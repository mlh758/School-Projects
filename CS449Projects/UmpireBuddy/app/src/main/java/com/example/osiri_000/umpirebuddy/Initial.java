package com.example.osiri_000.umpirebuddy;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

//REMEMBER TO CHECK OUT onPause METHOD
public class Initial extends Activity {

    private int balls;
    private int strikes;
    private int outs;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_initial);
        SharedPreferences sharedPref = this.getSharedPreferences("pref_general", Context.MODE_PRIVATE);
        outs = sharedPref.getInt(getString(R.string.total_outs), 0);
        balls = 0;
        strikes = 0;
        UpdateDisplay();
    }

    @Override
    protected void onDestroy() {
        SharedPreferences sharedPref = this.getSharedPreferences("pref_general", Context.MODE_PRIVATE);
        SharedPreferences.Editor prefEditor = sharedPref.edit();
        prefEditor.putInt(getString(R.string.total_outs), outs);
        prefEditor.commit();
        super.onDestroy();
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        outState.putInt("Strikes", strikes);
        outState.putInt("Balls", balls);
        outState.putInt("Outs", outs);
        super.onSaveInstanceState(outState);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);
        strikes = savedInstanceState.getInt("Strikes");
        balls = savedInstanceState.getInt("Balls");
        outs = savedInstanceState.getInt("Outs");
        SharedPreferences defaults = PreferenceManager.getDefaultSharedPreferences(this);
        UpdateDisplay();
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
                Intent settingsIntent = new Intent(Initial.this, SettingsActivity.class);
                startActivity(settingsIntent);
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
            SharedPreferences defaults = PreferenceManager.getDefaultSharedPreferences(this);
            if(defaults.getBoolean("walk_audio_pref", false)){
                MediaPlayer player = MediaPlayer.create(Initial.this, R.raw.walk);
                player.start();
            }


        }

    }

    public void sendStrike(View view) {
        //Handler for strike event
        strikes++;
        UpdateDisplay();
        if(strikes == 3){
            outs++;
            AlertDialog dialog = MessageBuilder(this,getString(R.string.out_msg) );
            dialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
                @Override
                public void onDismiss(DialogInterface dialogInterface) {
                    ResetDisplay();
                }
            });

            dialog.show();
            SharedPreferences defaults = PreferenceManager.getDefaultSharedPreferences(this);
            if(defaults.getBoolean("out_audio_pref", false)){
                MediaPlayer player = MediaPlayer.create(Initial.this, R.raw.out);
                player.start();
            }

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
        TextView outValue = (TextView) findViewById(R.id.out_count);
        strikeValue.setText(Integer.toString(strikes));
        ballValue.setText(Integer.toString(balls));
        outValue.setText(Integer.toString(outs));
    }

    private void ResetDisplay(){
        balls = strikes = 0;
        UpdateDisplay();
    }

}

