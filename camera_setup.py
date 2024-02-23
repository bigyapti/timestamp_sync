# camera_setup.py
import os
import pypylon.pylon as py

def setup_cameras(num_cameras):
    os.environ["PYLON_CAMEMU"] = f"{num_cameras}"
    tlf = py.TlFactory.GetInstance()
    cam_array = py.InstantCameraArray(num_cameras)

    for idx, cam in enumerate(cam_array):
        cam.Attach(tlf.CreateDevice(tlf.EnumerateDevices()[idx]))
        cam.Open()
        cam.SetCameraContext(idx)
        cam.TriggerSelector.SetValue("FrameStart")
        cam.TriggerMode.SetValue("On")
        cam.TriggerSource.SetValue("Software")
        cam.ExposureTimeRaw.Value = 10000

    return cam_array
