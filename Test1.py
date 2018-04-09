#https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key=AIzaSyAQHV19y7h6YyHSoGLEH_4fyXNqEN8C3Hs
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
              "Python is 10 seconds awsm!",
              icon_path="custom.ico",
              duration=10)
toaster.show_toast("Hello World!!!",
             "Python is awsm by default!")