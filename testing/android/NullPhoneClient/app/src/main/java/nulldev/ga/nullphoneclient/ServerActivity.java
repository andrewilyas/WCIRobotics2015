package nulldev.ga.nullphoneclient;

import android.content.Context;
import android.hardware.Camera;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Surface;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

import nulldev.ga.nullphoneclient.lib.LibNullWIFISocketClient;


public class ServerActivity extends ActionBarActivity {

    public String IP = "0.0.0.0";

    LibNullWIFISocketClient WIFIClient;

    ScheduledExecutorService ses = Executors.newSingleThreadScheduledExecutor();

    Camera c;
    SurfaceView cameraView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_server);

        //Get IP from previous activity
        IP = getIntent().getStringExtra(LaunchActivity.EXTRA_IP);

        //Add the IP to the label
        TextView textLabel = (TextView) findViewById(R.id.serverTitle);
        textLabel.setText(textLabel.getText() + " " + IP);

        //Start the server
        WIFIClient = new LibNullWIFISocketClient();
        WIFIClient.giveActivity(this);
        WIFIClient.serverPort = 2332;
        WIFIClient.connect(IP);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_server, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            showLongToast("There are currently no settings to configure 😛");
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
    @Override
    protected void onResume() {
        c = Camera.open();
        super.onResume();

        cameraView = (SurfaceView) findViewById(R.id.cameraView);
        Log.i("NullPhoneClient", "VIEW: " + cameraView.getHolder());
        cameraView.getHolder().setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
        try {
            c.setPreviewDisplay(cameraView.getHolder());
        } catch (IOException e) {
            e.printStackTrace();
        }

        Log.i("NullPhoneClient", "cameraView: " + cameraView);

        //Start taking pictures
        ses.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                takePicture();
            }
        }, 0, 1, TimeUnit.SECONDS);
    }

    @Override
    public void onPause()
    {
        super.onPause();

        //Stop taking pictures
        ses.shutdown();

        //Stop the server...
        WIFIClient.stop();
    }

    public void onStopButton(View view) {
        //Just use finish which will execute onPause() above...
        finish();
    }

    public void showLongToast(final String text) {
        this.runOnUiThread(new Runnable() {
            public void run() {
                int duration = Toast.LENGTH_LONG;
                Toast toast = Toast.makeText(getApplicationContext(), text, duration);
                toast.show();
            }
        });
    }

    public void takePicture(){
        try {
            c.stopPreview();
        } catch (Exception e){
            // ignore: tried to stop a non-existent preview
        }

        c.setParameters(c.getParameters());
        c.startPreview();
        c.takePicture(null, null, jpegCallback);
    }

    Camera.PictureCallback jpegCallback = new Camera.PictureCallback() {
        public void onPictureTaken(byte[] data, Camera camera) {
            //data is the binary JPEG data...

            //Encode the image into Base64
            String encodedImage = Base64.encodeToString(data, Base64.DEFAULT);

            //Send the image
            WIFIClient.sendCommand(encodedImage);

            Log.i("NullPhoneClient", "Sent: " + encodedImage);
        }
    };

}