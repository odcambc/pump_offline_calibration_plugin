
## Pioreactor offline pump calibration plugin

This plugin creates a new workflow for calibrating pumps using offline measurements rather than interactive prompts.

This will allow users to create a more flexible calibration using a set of their own measurements. Make sure to evaluate the quality of the calibration based on the fit produced.

Note that the PWM frequency and duty cycles should be the same as those used to generate the measurements.

This is a drop-in replacement for the standard pump calibration, and does not change the behavior of dosing after calibration. 

## Run your calibration

Type into your command line:

```
pio run pump_offline_calibration
```

To perform this calibration, first manually perform a series of dosings using the fixed time option, then measure the amount of water pumped. After running the above command, you will be prompted to enter the times and amounts.