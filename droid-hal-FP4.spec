# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device FP4
%define vendor fairphone

%define vendor_pretty Fairphone
%define device_pretty Fairphone 4
%define droid_target_aarch64 1 
%define installable_zip 1

%define straggler_files \
   /bugreports \
   /cache \
   /d \
   /sdcard \
%{nil}

%include rpm/dhd/droid-hal-device.inc
