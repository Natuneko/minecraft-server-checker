from mcstatus import MinecraftServer
from concurrent.futures import ThreadPoolExecutor
import os

os.system("cls & title Minecraft Server Checker")

def check_server(address):
    out = open('all.txt', 'a', encoding='UTF-8')
    server = MinecraftServer.lookup(address)
    status = server.status()
    online_user = str(["{}".format(player.name)for player in status.players.sample] if status.players.sample is not None else "[]")
    print(" IP:",address,"\n","VERSION:",status.version.name,"\n","PLAYERS:",str(status.players.online)+"/"+str(status.players.max),"\n","ONLINE PLAYERS:",online_user,"\n","MOTD:",status.description,"\n","=================================================")
    # print("VERSION:",status.version.name)
    # print("PLAYERS:",str(status.players.online)+"/"+str(status.players.max))
    # print("ONLINE PLAYERS:",status.players.sample)
    # print("MOTD:",status.description)
    # print("=================================================")
    # out.write("IP: "+address+"\n")
    # out.write("VERSION: "+status.version.name+"\n")
    # out.write("PLAYERS: "+str(status.players.online)+"/"+str(status.players.max)+"\n")
    # out.write("ONLINE PLAYERS: "+str(["{}".format(player.name)for player in status.players.sample])+"\n")
    # out.write("MOTD: "+status.description+"\n")
    # out.write("=================================================\n")
    out.write("IP: "+address+"\n"+"VERSION: "+status.version.name+"\n"+"PLAYERS: "+str(status.players.online)+"/"+str(status.players.max)+"\n"+"ONLINE PLAYERS: "+online_user+"\n"+"MOTD: "+status.description+"\n"+"=================================================\n")
    out.close()
    ver_out = open("ver/"+status.version.name+".txt","a",encoding="UTF_8")
    ver_out.write("IP: "+address+"\n"+"VERSION: "+status.version.name+"\n"+"PLAYERS: "+str(status.players.online)+"/"+str(status.players.max)+"\n"+"ONLINE PLAYERS: "+online_user+"\n"+"MOTD: "+status.description+"\n"+"=================================================\n")
    ver_out.close()
    if len(status.players.sample) > 0:
        user_list = open("user.txt","a",encoding="UTF_8")
        user_list.write("IP: "+address+"\n"+"VERSION: "+status.version.name+"\n"+"PLAYERS: "+str(status.players.online)+"/"+str(status.players.max)+"\n"+"ONLINE PLAYERS: "+online_user+"\n"+"MOTD: "+status.description+"\n"+"=================================================\n")
        user_list.close()

try:
    iplist = open("iplist.txt","r",encoding="UTF_8")
    ip_num = len(open("iplist.txt","r",encoding="UTF_8").readlines())
    os.system(f"cls & title Minecraft Server Checker ^| 0/{ip_num}")
except FileNotFoundError:
    print("Not Found iplist.txt")
    _ = open("iplist.txt","w")
    _.close()
    print("Generated iplist.txt")
    exit()

if os.path.exists("ver") == False:
    os.mkdir("ver")

while True:
    try:
        thread_num = int(input("thread: "))
        tpe = ThreadPoolExecutor(max_workers=thread_num)
        break
    except ValueError:
        print("Error, please try again")
    except KeyboardInterrupt:
        exit()

count = 0

while True:
    ip = iplist.readline().replace("\n","")
    if ip:
        tpe.submit(check_server,ip)
        count += 1
        os.system(f"title Minecraft Server Checker ^| {count}/{ip_num}")

    else:
        break

tpe.shutdown()
print("finish")