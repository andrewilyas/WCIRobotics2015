package nulldev.ga.nullphoneclient;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.security.Key;


public class LaunchActivity extends ActionBarActivity {

    public final static String EXTRA_IP = "nulldev.ga.nullphoneclient.IP";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_launch);

        //Start server when the enter button is pressed
        EditText editText = (EditText) findViewById(R.id.editIP);
        editText.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent caughtEvent) {
                boolean handled = false;
                if (actionId == 0) {
                    startServer(findViewById(R.id.editIP));
                    handled = true;
                }
                return handled;
            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_launch, menu);
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
            int duration = Toast.LENGTH_LONG;
            Toast toast = Toast.makeText(getApplicationContext(), "There are currently no settings to configure 😛", duration);
            toast.show();
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void startServer(View view) {
        //Get the IP
        EditText editText = (EditText) findViewById(R.id.editIP);
        String ip = editText.getText().toString();
        //Log the IP
        Log.i("NullPhoneClient", "IP is: " + ip);

        //Switch the server activity
        Intent intent = new Intent(this, ServerActivity.class);
        //Copy the IP to the intent
        intent.putExtra(EXTRA_IP, ip);
        //Start the activity
        startActivity(intent);
    }
}
