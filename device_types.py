DEVICE_TYPES = {
  "mock_device": {
      "get": {},
      "change_status": {
          "new_status": "boolean"
      },
      "invert_status": {}
  },
  "ledcontrol": {
      "get":{},
      "change_rgb":{
          "color": "rgb"
      },
      "change_brightness":{
          "brightness": "number"
      },
      "change_toWarm":{},
      "change_toWhite":{},
      "change_turnOff":{},
      #"start_animation":{
          #"animation": ["rainbow", "fisch"]
      #},
      "start_animation_rainbowCycle":{}
  }
}
