package com.example.osiri_000.umpirebuddy;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
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
        switch(item.getItemId()){
            case R.id.action_settings:
                return true;
            case R.id.action_about:
                Intent intent = new Intent(Initial.this, About.class);
                startActivity(intent);
                return true;
            case R.id.action_reset:
                ResetDisplay();
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

    public void sendBall(View view) {
        //Handler for ball event
        balls++;
        UpdateDisplay();
        if (balls == 4) {
            AlertDialog dialog = MessageBuilder(this, getString(R.string.walk_msg));
            dialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
                @Override
                public void onDismiss(DialogInterface dialogInterface) {
                    ResetDisplay();
                }
            });

            dialog.show();

        }

    }

    public void sendStrike(View view) {
        //Handler for strike event
        strikes++;
        UpdateDisplay();
        if(strikes == 3){
            AlertDialog dialog = MessageBuilder(this,getString(R.string.out_msg) );
            dialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
                @Override
                public void onDismiss(DialogInterface dialogInterface) {
                    ResetDisplay();
                }
            });
            dialog.show();
        }
    }






    private AlertDialog MessageBuilder(Context sender, CharSequence message){
        //Function for building messages in event handlers above
        AlertDialog.Builder builder = new AlertDialog.Builder(sender);
        builder.setMessage(message);
        builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                //Do nothing, just acknowledge the dialog
            }
        });
        return builder.create();
        }

    private void UpdateDisplay(){
        TextView ballValue = (TextView) findViewById(R.id.ball_count);
        TextView strikeValue = (TextView) findViewById(R.id.strike_count);
        strikeValue.setText(Integer.toString(strikes));
        ballValue.setText(Integer.toString(balls));
    }

    private void ResetDisplay(){
        balls = strikes = 0;
        UpdateDisplay();
    }

}

