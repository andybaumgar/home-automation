import re
import subprocess


def get_usb_devices():
    device_re = re.compile(
        b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$",
        re.I,
    )
    df = subprocess.check_output("lsusb")
    devices = []
    for i in df.split(b"\n"):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo["device"] = "/dev/bus/usb/%s/%s" % (
                    dinfo.pop("bus"),
                    dinfo.pop("device"),
                )
                devices.append(dinfo)

    print(devices)
    return devices


def get_adafruit_feather(devices):
    for device in devices:
        if device["tag"].decode("utf-8") == "Adafruit Feather M0":
            return device["device"].replace("/b'", "/").replace("'", "")
    return None


if __name__ == "__main__":
    sample_devices = [
        {
            "id": b"239a:800b",
            "tag": b"Adafruit Feather M0",
            "device": "/dev/bus/usb/b'001'/b'009'",
        },
        {
            "id": b"0424:7800",
            "tag": b"Microchip Technology, Inc. (formerly SMSC) ",
            "device": "/dev/bus/usb/b'001'/b'004'",
        },
        {
            "id": b"0424:2514",
            "tag": b"Microchip Technology, Inc. (formerly SMSC) USB 2.0 Hub",
            "device": "/dev/bus/usb/b'001'/b'003'",
        },
        {
            "id": b"0424:2514",
            "tag": b"Microchip Technology, Inc. (formerly SMSC) USB 2.0 Hub",
            "device": "/dev/bus/usb/b'001'/b'002'",
        },
        {
            "id": b"1d6b:0002",
            "tag": b"Linux Foundation 2.0 root hub",
            "device": "/dev/bus/usb/b'001'/b'001'",
        },
    ]

    print(get_adafruit_feather(sample_devices))
