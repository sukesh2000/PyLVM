import os

pvName = input("Enter a name of the device [/dev/sda]: ") or "/dev/sda"
volGrp = input("Enter a volume group name[vg1]: ") or "vg1"
lvName = input("Enter a logical volume name[lv1]: ") or "lv1"
lvSize = input("Enter the size of the logical volume[1G]: ") or "1G"
mount = input("Enter the directory to mount on[/lvm1]: ") or "/lvm1"

os.system("pvcreate {}".format(pvName))
print("-------Physical Volume Created---------")
os.system("vgcreate {} {}".format(volGrp, pvName))
print("-------Volume Group Created---------")
os.system("lvcreate --size {} --name {} {}".format(lvSize, lvName, volGrp))
print("-------Logical Volume Created---------")
print("-------Formatting Using EXT4 File System---------")
os.system("mkfs.ext4 /dev/{}/{}".format(volGrp, lvName))
os.system("mount /dev/{}/{} {}".format(volGrp, lvName, mount))
print("-------Mounted the new LVM---------")