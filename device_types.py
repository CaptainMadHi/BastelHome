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
      "set_color":{
          "color": "rgb"
      },
      "set_brightness":{
          "brightness": "number"
      },
      "white_light":{},
      "warm_light":{},
      "turn_off":{},
      "start_animation":{
          "animation" : ["Static", "RainbowChase", "RainbowCycle", "TheaterChase"]
      },
      "set_Led_Count(number)":{
          "Number of LEDs": "number"
      }
  },
  "surveillance_camera":{
      "get":{},
      "capturePhoto":{}
  }
}