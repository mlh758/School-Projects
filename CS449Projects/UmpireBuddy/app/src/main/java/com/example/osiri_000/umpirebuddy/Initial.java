package com.example.osiri_000.umpirebuddy;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;


public class Initial extends Activity {

    private int balls;
    private int strikes;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_initial);
        balls = 0;
        strikes = 0;
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.initial, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    public void sendBall(View view) {
        AlertDialog showBall = MessageBuilder(this, "Ball", 1);
        final Context sender = this;
        showBall.setOnDismissListener(new DialogInterface.OnDismissListener() {
            @Override
            public void onDismiss(DialogInterface dialogInterface) {
                if(balls==4){
                    AlertDialog showOut = MessageBuilder(sender, "WALK!", 3);
                    showOut.show();
                }
            }
        });
        showBall.show();
    }

    public void sendStrike(View view) {
        final Context sender = this;
        AlertDialog showStrike = MessageBuilder(sender, "Strike", 0);
        showStrike.setOnDismissListener(new DialogInterface.OnDismissListener() {
            @Override
            public void onDismiss(DialogInterface dialogInterface) {
                if(strikes==3){
                    AlertDialog showOut = MessageBuilder(sender, "OUT!", 3);
                    showOut.show();
                }
            }
        });
        showStrike.show();
    }




    private AlertDialog MessageBuilder(Context sender, CharSequence message, int level){
        AlertDialog.Builder builder = new AlertDialog.Builder(sender);
        builder.setMessage(message);
        switch(level) {
            case 0:
                //Building Strike Dialog
                builder.setPositiveButton(R.string.dialog_ok, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        strikes += 1;
                        TextView strikeValue = (TextView) findViewById(R.id.strike_count);
                        strikeValue.setText(Integer.toString(strikes));
                    }
                });
                break;
            case 1:
                //Building Ball Dialog
                builder.setPositiveButton(R.string.dialog_ok, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        balls += 1;
                        TextView ballValue = (TextView) findViewById(R.id.ball_count);
                        ballValue.setText(Integer.toString(balls));
                    }
                });
                break;
            default:
                //Walk or Out, reset the counts
                builder.setPositiveButton(R.string.dialog_ok, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int id) {
                        TextView ballValue = (TextView) findViewById(R.id.ball_count);
                        TextView strikeValue = (TextView) findViewById(R.id.strike_count);
                        balls = 0;
                        strikes = 0;
                        ballValue.setText("0");
                        strikeValue.setText("0");

                    }
                });
                break;
        }
        builder.setNegativeButton(R.string.dialog_cancel, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int id) {
                // User cancelled the dialog
            }
        });

        return builder.create();
        }

}

