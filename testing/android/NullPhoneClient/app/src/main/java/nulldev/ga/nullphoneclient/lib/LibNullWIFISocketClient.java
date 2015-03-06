package nulldev.ga.nullphoneclient.lib;

import android.content.Context;
import android.util.Log;
import android.widget.Toast;

import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.LinkedList;
import java.util.Queue;

import nulldev.ga.nullphoneclient.ServerActivity;

/**
 * Created by nulldev on 24/01/15.
 *
 * Based On: https://thinkandroid.wordpress.com/2010/03/27/incorporating-socket-programming-into-your-applications/
 */

//Library to connect to the server via socket. (WIFI)
public class LibNullWIFISocketClient {

    private ServerActivity serverActivity;
    private String serverIpAddress = "";
    public int serverPort = 0;

    public Queue<String> commandQueue = new LinkedList<String>();

    public boolean connected = false;

    Thread clientThread = new Thread(new ClientThread());

    PrintWriter out;
    Socket socket;

    public void giveActivity(ServerActivity serverActivity) {
        this.serverActivity = serverActivity;
    }

    public void connect(String ip) {
        if (!connected) {
            serverIpAddress =ip;
            if (!serverIpAddress.equals("")) {
                clientThread.start();
            } else {
                serverActivity.showLongToast("IP cannot be empty!");
                serverActivity.onPause();
            }
        } else {
            serverActivity.showLongToast("The server is still active, please wait a moment for it to stop!");
            serverActivity.onPause();
        }
    }

    public void stop() {
        connected = false;
    }

    public void sendCommand(String command) { commandQueue.add(command); }

    public class ClientThread implements Runnable {

        public void run() {
            try {
                InetAddress serverAddr = InetAddress.getByName(serverIpAddress);
                Log.i("LibNullWIFISocketClient", "Connecting...");
                socket = new Socket(serverAddr, serverPort);
                connected = true;

                if(connected) {
                    out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket
                            .getOutputStream())), true);
                    while (connected) {
                        try {
                            //Loop command queue and remove commands executed
                            if(!commandQueue.isEmpty())
                                out.println(commandQueue.poll());
                        } catch (Exception e) {
                            Log.e("LibNullWIFISocketClient", "Connection Closed", e);
                            connected = false;
                            serverActivity.showLongToast("Connection closed!");
                            serverActivity.onPause();
                        }
                    }
                    //Resource leaks suck :(
                    out.close();
                    socket.close();
                    Log.i("LibNullWIFISocketClient", "Server Stopped!");
                    serverActivity.onPause();
                }
            } catch (Exception e) {
                Log.e("LibNullWIFISocketClient", "Connection Closed", e);
                connected = false;

                //===ADDED TO LIBRARY===
                serverActivity.showLongToast("Unable to connect to IP!");
                serverActivity.onPause();
            }
        }
    }
}
