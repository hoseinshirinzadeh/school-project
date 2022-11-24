import time

while True:
    
#section one
    esm = input("esm khod ra vared konid:")
    
    no = input("addad aval ra vared konid:")
    no = float(no)
    
    time.sleep(2)
    print("number one:",no)

    nt = input("addad dovom ra vaded konid:")
    nt = float(nt)

    time.sleep(3)
    print("number two:",nt)

#setcion two
    print("halat haye mored nazar:zarb,taghsim,jamh,menha")
    halat = input("halat mored nazar riazi ra vared konid:")
    
    if halat == "zarb":
        print(no * nt)
        print("mamnoon az barna man estefade kardid",esm)

    elif halat == "taghsim":
        print(no / nt)
        print("mamnoon az barna man estefade kardid",esm)

    elif halat == "jamh":
        print(no + nt)
        print("mamnoon az barna man estefade kardid",esm)
    
    elif halat == "menha":
        print(no - nt)
        print("mamnoon az barna man estefade kardi",esm)

    else:
        print("kari soorat naghereft")
        print("mamnoon az barna man estefade kardid",esm)

#create by hosein shirinzadeh
#school project

