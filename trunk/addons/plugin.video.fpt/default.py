import urllib,urllib2,re,sys,xbmcplugin,xbmcgui
import cookielib,os,string,cookielib,StringIO
import os,time,base64,logging
import xbmcaddon, mechanize
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

fpt=xbmcaddon.Addon(id='plugin.video.fpt')
pluginhandle = int(sys.argv[1])

def login():
	urlogin = 'http://www.fastpasstv.eu/register'
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
 	values = {'login': uname,'password': pwd}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(urlogin, data, headers)
	response = urllib2.urlopen(req)

def geturl(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        return link

def redirect(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        gurl=response.geturl()
        return gurl

def xbmcpath(path,filename):
     translatedpath = os.path.join(xbmc.translatePath( path ), ''+filename+'')
     return translatedpath

def openfile(filename):
     fh = open(filename, 'r')
     contents=fh.read()
     fh.close()
     return contents

def save(filename,contents):  
     fh = open(filename, 'w')
     fh.write(contents)  
     fh.close()

fptpath = 'special://temp/'
translatedfptpath = xbmcpath(fptpath,'')
referer = xbmcpath(fptpath,'ref.txt')

def CATS():
        addDir('Most Popular TV Shows Today','http://www.fastpasstv.ms/',14,'')
        addDir('Most Popular Movies Today','http://www.fastpasstv.ms/',5,'')
        addDir('Latest Added TV Shows','http://www.fastpasstv.ms/tv/',4,'')
        addDir('Latest Added Movies','http://www.fastpasstv.ms/movies',20,'')
        addDir('Latest Added Documentaries','http://www.fastpasstv.ms/documentaries',22,'')
        addDir('All TV Shows','http://www.fastpasstv.ms/tv',2,'')
	addDir('All Movies','http://www.fastpasstv.ms/movies',1,'')
	addDir('All Documentaries','http://www.fastpasstv.ms/documentaries',1,'')
	addDir('Search','http://www.fastpasstv.ms/',9,'')

def NEWEP(url,name):
        link= geturl(url)
      	tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in tvs:
		addDir(name,'http://www.fastpasstv.ms/tv/'+url2,18,'')

def MOVALL(url,name):
        link= geturl(url)
     	mvs=re.compile('<li><a href="(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(link)
	for url,name in mvs:
		addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.ms'+url,18,'')

def MOVLAT(url,name):
        link= geturl(url)
	all = re.compile('<p><b>Latest additions</b>.+?<ul class="pagination">', re.DOTALL).findall(link)
      	mv=re.compile('<title>(.+?)</title>\n		<link>http://www.fastpasstv.eu/movies/(.+?)/</link>').findall(link)
	for name,url in mv:
		addDir(name.replace('&amp;','&'),'http://www.fastpasstv.ms/movies/'+url,18,'')

def DOCLAT(url,name):
        link= geturl(url)
	all = re.compile('<p><b>Latest additions</b>.+?<ul class="pagination">', re.DOTALL).findall(link)
      	doc=re.compile('<title>(.+?)</title>\n		<link>http://www.fastpasstv.eu/documentaries/(.+?)/</link>').findall(link)
	for name,url in doc:
		addDir(name.replace('&amp;','&'),'http://www.fastpasstv.ms/documentaries/'+url,18,'')

def X2(url,name): 
        link= geturl(url)
     	list=re.compile('<li><a href="(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(link)
	for url,name in list:
		addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.ms'+url,21,'')

def Y1(url,name):
        link= geturl(url)
	all = re.compile('	<b>Latest additions</b>:.+?<ul class="pagination">', re.DOTALL).findall(link)
      	tvs=re.compile('<a href="(.+?)">(.+?)</a>').findall(all[0])
	for url,name in tvs:
		addDir(name.replace('&amp;','&'),'http://www.fastpasstv.ms'+url,18,'')

def Y2(url,name):
        link= geturl(url)
      	mvs=re.compile('<li><a href="/movies/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in mvs:
		addDir(name,'http://www.fastpasstv.ms/movies/'+url2,18,'')

def Y3(url,name):
        link= geturl(url)
      	tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in tvs:
		addDir(name,'http://www.fastpasstv.ms/tv/'+url2,18,'')

def Y3MOV(url,name):
	i=0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        ref=response2.geturl()
	save(referer,ref)
        link=response2.read()
	nova=re.compile('<b>Novamov</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	mega=re.compile('<b>Megavideo</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	woot=re.compile('<b>Wootly</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	fv2=re.compile('<b>VidX.+?FLV.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	dv=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	dv1=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      	dv2=re.compile('<b>VidX.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      	vidbx=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	vidbx1=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      	vidbx2=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      	wise=re.compile('<b>WiseVid</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	putloc=re.compile('<b>Putlocker </b></td>\n									<td class="siteparts" style="width:165px;"><a href="(.+?)"').findall(link)
       	apex=re.compile('<b>apexvid.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	for url in apex:
		i=i+1
		addDir('Apexvid (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),24,'')
	for url in nova:
		i=i+1
		addDir('Novamov (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),12,'')
	for url in woot:
		i=i+1
		addDir('Wootly (mp4) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),7,'')
	for url in dv1:
		i=i+1
		addDir('DivxDen (avi) Pt 1 #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),8,'')
	for url in dv2:
		i=i+1
		addDir('DivxDen (avi) Pt 2 #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),8,'')
	for url in dv:
		i=i+1
		addDir('DivxDen (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),8,'')
	for url in vidbx:
		i=i+1
		addDir('VidBux (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),10,'')
	for url in vidbx1:
		i=i+1
		addDir('VidBux (avi) Pt 1 #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),10,'')
	for url in vidbx2:
		i=i+1
		addDir('VidBux (avi) Pt 2 #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),10,'')
	for url in putloc:
		i=i+1
		addDir('PutLocker (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),23,'')
	for url in wise:
		i=i+1
		addDir('Wisevid (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),19,'')
	for url in mega:
		i=i+1
		addDir('Megavideo (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),15,'')

def Y3TV(url,name):
	i=0
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        ref=response2.geturl()
	save(referer,ref)
        link=response2.read()
	mega=re.compile('<b>Megavideo</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	woot=re.compile('<b>Wootly</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)

      	dv=re.compile('<b>Vidxden.+?DivX.+?</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
	dvflash=re.compile('<b>Vidxden.+?Flash.+?</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)


      	vidbx=re.compile('<b>VidBux.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	vidbx2=re.compile('<b>VidBux.+?FLV.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)

       	wise=re.compile('<b>WiseVid</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	putloc=re.compile('<b>putlocker.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       	apex=re.compile('<b>apexvid.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)

	divxavi=re.compile('<b>Divxden.+?DivX.+?</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
	divxflash=re.compile('<b>Divxden.+?Flash.+?</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)

       	new2=re.compile('<b>Put.+?</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	new3=re.compile('<b>Vidbu.+?</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	new4=re.compile('<b>Novamov</b></td>\n.+?<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	for url in apex:
		i=i+1
		addDir('Apexvid (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),24,'')

	for url in dv:
		i=i+1
		addDir('Vidxden (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),8,'')
	for url in dvflash:
		i=i+1
		addDir('Vidxden (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),27,'')
	for url in mega:
		i=i+1
		addDir('Megavideo (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),15,'')
	for url in woot:
		i=i+1
		addDir('Wootly (mp4) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),7,'')
	for url in putloc:
		i=i+1
		addDir('PutLocker (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),23,'')
	for url in vidbx:
		i=i+1
		addDir('VidBux (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),10,'')
	for url in vidbx2:
		i=i+1
		addDir('VidBux (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),25,'')
	for url in divxavi:
		i=i+1
		addDir('Divxden (avi) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),8,'')
	for url in divxflash:
		i=i+1
		addDir('Divxden (flv) #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),27,'')
	for url in new2:
		i=i+1
		addDir('Putlocker #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),23,'')
	for url in new3:
		i=i+1
		addDir('Vidbux #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),10,'')
	for url in new4:
		i=i+1
		addDir('Novamov #'+str(i),'http://www.fastpasstv.ms'+url.replace('/watch','/redirect'),12,'')

def PUTLOC(url,name):
        #login()
        link1 = geturl(url)
        link2 = redirect(url)
        try:
                hash=re.compile('type="hidden" value="(.+?)" name="hash"').findall(link1)[0]
        except:
                dialog = xbmcgui.Dialog()
                ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
                return

        values = {'hash': hash, 'confirm':'Continue as Free User'}
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent}
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
        data = urllib.urlencode(values)
        req = urllib2.Request(link2, data, headers)
        response = urllib2.urlopen(req)
        link = response.read()
        code = re.compile("stream=(.+?)'").findall(link)
        req = urllib2.Request('http://www.putlocker.com/get_file.php?stream='+code[0])
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        link=response.read()
        finalurl = re.compile('<media:content url="(.+?)"').findall(link)[0]
        Play(finalurl)

def WOOT(url,name):
	#login()	
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	if 'mp4' in fcodenm:
		file=re.compile("mp4(.+?)182|file").findall(link)[0]
		cleanup=file.replace('|',' ').replace('||',' ')
		hashlong = cleanup[-57:].replace(' ','')	
		hashshort =  re.compile("ltas(.+?)flvplayer").findall(link)[0]
		if hashshort == '||' :
			hashshort = 's1'
    		finalurl = 'http://'+hashshort.replace('|','')+'.wootly.com:182/d/'+hashlong+'/'+ 'video.mp4'
		Play(finalurl)
		return
	else:
		file=re.compile("Stage6(.+?)182|file").findall(link)[0]
		cleanup=file.replace('|',' ').replace('||',' ')
		hashlong = cleanup[-57:].replace(' ','')	
		hashshort =  re.compile("wootly(.+?)divx").findall(link)[0]
		if hashshort == '||' :
			hashshort = 's1'
    		finalurl = 'http://'+hashshort.replace('|','')+'.wootly.com:182/d/'+hashlong+'/'+ 'video.avi'
		Play(finalurl)

def WOOTAVI(url,name):
	#login()	
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("Stage6(.+?)182|file").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-57:].replace(' ','')	
	hashshort =  re.compile("wootly(.+?)divx").findall(link)[0]
	if hashshort == '||' :
		hashshort = 's1'
    	finalurl = 'http://'+hashshort.replace('|','')+'.wootly.com:182/d/'+hashlong+'/'+ 'video.mp4'
	Play(finalurl)

def APEX(url,name):
	#login()	
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)

	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("mp4(.+?)182.+?file").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-57:].replace(' ','')	
	hashshort =  re.compile("video(.+?)flvplayer").findall(link)[0]
	if hashshort == '||' :
		hashshort = 's1'
    	finalurl = 'http://'+hashshort.replace('|','')+'.apexvid.com:182/d/'+hashlong+'/'+ 'video.mp4'
	Play(finalurl)

def VIDSDIVX(url,name):
	#login()
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)

	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file = re.compile("Stage6(.+?)364|divxden").findall(link)[0]
	print file
	cleanup = file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-46:].replace(' ','')
	hashshort =  re.compile('divxden(.+?)src').findall(link)[0]
   	finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:364/d/'+hashlong+'/'+ fcodenm
	Play(finalurl)

def VIDXFLV(url,name):
	#login()
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)

	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file = re.compile("image(.+?)364|divxden").findall(link)[0]
	print file
	cleanup = file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-46:].replace(' ','')
	hashshort =  re.compile('divxden(.+?)file').findall(link)[0]
   	finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:364/d/'+hashlong+'/'+ fcodenm
	Play(finalurl)
 
def VIDBUX(url,name):
	#login()
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }

	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("vidbux(.+?)182|file").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-41:].replace(' ','')
	hashshort =  re.compile('</div><!-- <img src="http://(.+?).vidbux.com').findall(link)[0]
   	finalurl = 'http://'+hashshort+'.vidbux.com:182/d/'+hashlong+'/'+ fcodenm + '?start=0'
	Play(finalurl)

def VIDBUX2(url,name):
	#login()
	link1 = geturl(url)
	link2 = redirect(url)
	try:
		fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link1)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("FastPassTv",'The file has been removed due to copyright.')
		return

	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link1)[0]
	refer=openfile(referer)

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)

	data = urllib.urlencode(values)
	req = urllib2.Request(link2, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("'(.+?)182").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-41:].replace(' ','')
	hashshort =  re.compile("182(.+?)file").findall(link)[0]
   	finalurl = 'http://'+hashshort.replace('|','')+'.vidbux.com:182/d'+hashlong+'/'+ fcodenm
	Play(finalurl)

def Nova(url,name):
        link= geturl(url)
	finalurl=re.compile('flashvars.file="(.+?)"').findall(link)[0]
	Play(finalurl)

def Mega(url,name):
	login()
	gurl = redirect(url)
	code = gurl[-8:]
        try:
                req = urllib2.Request("http://www.megavideo.com/xml/videolink.php?v="+code)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                req.add_header('Referer', 'http://www.megavideo.com/')
                lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
                errort = re.compile(' errortext="(.+?)"').findall(response)
                if len(errort) > 0: addLink(errort[0],'http://novid.com','')
                else:
                        s = re.compile(' s="(.+?)"').findall(response)
                        k1 = re.compile(' k1="(.+?)"').findall(response)
                        k2 = re.compile(' k2="(.+?)"').findall(response)
                        un = re.compile(' un="(.+?)"').findall(response)
                        finalurl = "http://www" + s[0] + ".megavideo.com/files/" + __calculateFileHash(un[0], k1[0], k2[0]) + "/?.flv"
			Play(finalurl)
        except: pass

def __calcDecriptionMix(hash, keyMix):
  """Mixes the decription keys into the hash and returns the updated hash
  @param hash: the hash to merge the keys into
  @param keyMix: the array of keys to mix"""
  for i in range(128):
    hash[i] = str(int(hash[i]) ^ int(keyMix[i + 256]) & 1)
  return "".join(hash)

def __toHexDecriptionString(binaryChunks):
  """Converts an array of binary strings into a string of the corresponding hex chunks merged
  This method will first loop through the binary strings converting each one into it's correspondent
  hexadecimal string and then merge the resulting array into a string
  @param binaryChunks: an array of binary strings
  @return: a string of the corresponding hexadecimal strings, merged"""
  hexChunks = []
  for binChunk in binaryChunks:
    hexChunks.append("%x" % int(binChunk, 2))    
  return "".join(hexChunks)

def __doDecriptionChunks(binaryMergedString):
  """Break a string of 0's and 1's in pieces of 4 chars
  @param binaryMergedString: a string of 0's and 1's to break in 4-part pieces
  @return: an array of 4 character parts of the original string"""
  binaryChunks = []
  for index in range(0, len(binaryMergedString), 4):
    binaryChunk = binaryMergedString[index:index + 4]
    binaryChunks.append(binaryChunk)
  return binaryChunks

def __doDecriptionSwaps(hash, keys):
  """Swap the first 256 indices from keys on the hash with the last 128 elements from the hash
  @param hash: the hash to do swaps on
  @param keys: the generated keys to use as indices for the swaps
  @return: hash after swaps"""
  for index in range(256, 0, -1):
    key = keys[index]
    swapTarget = index % 128
    oldHashKey = hash[key]
    hash[key] = hash[swapTarget]
    hash[swapTarget] = oldHashKey
  return hash

def __computeIndices(key1, key2):
  """Generate an array of 384 indices with values 0-127
  @param key1: first seed to generate indices from
  @param key2: second seed to generate indices from
  @return: an array of 384 indices with values between 0 and 127"""
  indices = []
  for i in range(384):
    key1 = (int(key1) * 11 + 77213) % 81371
    key2 = (int(key2) * 17 + 92717) % 192811
    indices.append((int(key1) + int(key2)) % 128)
  return indices

def __explodeBin(str1):
  # explode each char in str1 into it;s binary representation
  # and collect the result into __reg1
  __reg1 = []
  __reg3 = 0
  while (__reg3 < len(str1)):
    __reg0 = str1[__reg3]
    holder = __reg0
    if (holder == "0"):
      __reg1.append("0000")
    else:
      if (__reg0 == "1"):
        __reg1.append("0001")
      else:
        if (__reg0 == "2"): 
          __reg1.append("0010")
        else: 
          if (__reg0 == "3"):
            __reg1.append("0011")
          else: 
            if (__reg0 == "4"):
              __reg1.append("0100")
            else: 
              if (__reg0 == "5"):
                __reg1.append("0101")
              else: 
                if (__reg0 == "6"):
                  __reg1.append("0110")
                else: 
                  if (__reg0 == "7"):
                    __reg1.append("0111")
                  else: 
                    if (__reg0 == "8"):
                      __reg1.append("1000")
                    else: 
                      if (__reg0 == "9"):
                        __reg1.append("1001")
                      else: 
                        if (__reg0 == "a"):
                          __reg1.append("1010")
                        else: 
                          if (__reg0 == "b"):
                            __reg1.append("1011")
                          else: 
                            if (__reg0 == "c"):
                              __reg1.append("1100")
                            else: 
                              if (__reg0 == "d"):
                                __reg1.append("1101")
                              else: 
                                if (__reg0 == "e"):
                                  __reg1.append("1110")
                                else: 
                                  if (__reg0 == "f"):
                                    __reg1.append("1111")

    __reg3 = __reg3 + 1
  return list("".join(__reg1))

def __calculateFileHash(str1, key1, key2):
  # explode hex to bin strings, collapse to a string and return char array
  hash = __explodeBin(str1)
  # based on the keys, generate an array of 384 (256 + 128) values
  decriptIndices = __computeIndices(key1, key2)
  # from 256 to 0, swap hash[decriptIndices[x]] with hash[__reg3 % 128]
  hash = __doDecriptionSwaps(hash, decriptIndices)
  # replace the first 128 chars in hash with the formula:
  #  hash[x] = hash[x] * decriptIndices[x+256] & 1
  hash = __calcDecriptionMix(hash, decriptIndices)
  # split __reg12 in chunks of 4 chars
  chunks = __doDecriptionChunks(hash)  
  # convert each binary chunk to a hex string for the final hash
  return __toHexDecriptionString(chunks)

def SEARCH():
        keyb = xbmc.Keyboard('', 'Search FASTPASSTV')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
		values = {'input': encode,'submit': 'Search'}
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = { 'User-Agent' : user_agent }
		data = urllib.urlencode(values)
                req = urllib2.Request('http://www.fastpasstv.eu/search',data,headers)
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req).read()
     		tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(response)
     		docs=re.compile('li><a href="/documentaries/(.+?)">(.+?)<span class="epnum"').findall(response)
     		ctn=re.compile('<li><a href="/cartoons/(.+?)">(.+?)<span class="epnum">.+?</span></a>').findall(response)
     		mvs=re.compile('<li><a href="/movies/(.+?)">(.+?)<span class="epnum">.+?</span></a>').findall(response)
		for url,name in tvs:
			addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com/tv/'+url,21,'')
		for url,name in ctn:
			addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com/cartoons/'+url,21,'')
		for url,name in mvs:
			addDir(name,'http://www.fastpasstv.eu/movies/'+url,6,'')
		for url,name in docs:
			addDir(name,'http://www.fastpasstv.eu/documentaries/'+url,6,'')

def WISE(url,name):
	login()
	link1 = geturl(url)
	link2 = redirect(url)
	try:
			rawcode=re.compile("javascript:location.href='(.+?)'").findall(link1)[1]
			code=rawcode.replace('http://www.wisevid.com/play?v=','')
			ref=response.geturl()
			values = {'name': 'no','value': 'Yes, let me watch'}
			user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
			headers = { 'User-Agent' : user_agent, 'Referer': ref}
			data = urllib.urlencode(values)
			req = urllib2.Request(rawcode, data, headers)
			response = urllib2.urlopen(req)
			link = response.read()
			match=re.compile("getF(\(.+?)'").findall(link)[0]
			clean= match.replace("('","")
			finalurl=base64.decodestring(clean)
			Play(finalurl) 
	except: pass

	try:
			acode=re.compile('<input type="hidden" name="a" value="(.+?)" />').findall(link1)[0]
			vcode=re.compile('<input type="hidden" name="v" value="(.+?)" />').findall(link1)[0]
			url2='http://www.wisevid.com/play?v='+vcode
			values = {'a': acode,'v': vcode, 'no1' : 'Yes, let me watch'}
			user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
			headers = { 'User-Agent' : user_agent, 'Referer': 'http://www.wisevid.com/gate-way?v='+vcode}
			data = urllib.urlencode(values)
			req = urllib2.Request(url2, data, headers)
			response = urllib2.urlopen(req)
			link = response.read()
			match=re.compile("getF(\(.+?)'").findall(link)[0]
			clean= match.replace("('","")
			finalurl=base64.decodestring(clean)
			Play(finalurl)
	except: pass

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def addDir(name,url,mode,thumbnail,plot=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name,
                                                "plot": plot} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

class StopDownloading(Exception): 
        def __init__(self, value): 
            self.value = value 
        def __str__(self): 
            return repr(self.value) 

def Download(url, dest): 
        dp = xbmcgui.DialogProgress() 
        dp.create('Downloading', '', name) 
        start_time = time.time() 
        try: 
            urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time)) 
        except: 
            #delete partially downloaded file 
            while os.path.exists(dest): 
                try: 
                    print 'hello' 
                    break 
                except: 
                     pass 
            #only handle StopDownloading (from cancel), ContentTooShort (from urlretrieve), and OS (from the race condition); let other exceptions bubble 
            if sys.exc_info()[0] in (urllib.ContentTooShortError, StopDownloading, OSError): 
                return 'false' 
            else: 
                raise 
        return 'downloaded' 
         
def _pbhook(numblocks, blocksize, filesize, dp, start_time): 
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            # print ( 
                # percent, 
                # numblocks, 
                # blocksize, 
                # filesize, 
                # currently_downloaded, 
                # kbps_speed, 
                # eta, 
                # ) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs, e) 
            #print percent, mbs, e 
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
            raise StopDownloading('Stopped Downloading')

def Play(finalurl):
       	if (fpt.getSetting('download') == '0'):
                    dia = xbmcgui.Dialog()
                    ret = dia.select('Streaming Options', ['Play','Download'])
                    if (ret == 0):
			    addLink('Play',finalurl,'','','')
			    item = xbmcgui.ListItem(name)
          		    ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
                    elif (ret == 1):
                            path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                            Download(finalurl,path+name+'.flv')
                    else:
                            return
	elif (fpt.getSetting('download') == '1'):
 		addLink('Play',finalurl,'','','')
		item = xbmcgui.ListItem(name)
          	ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
        elif (fpt.getSetting('download') == '2'):
                path = xbmc.translatePath(os.path.join(fpt.getSetting('download_path'), name))
                Download(finalurl,path+name+'.flv')
        else:
        	return
 
def addLink(name,url,iconimage,plot,date):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty("IsPlayable","true");
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok

def check_settings():
		uname = fpt.getSetting('uname')
		pwd   = fpt.getSetting('pwd')
		if (not uname or uname == '') or (not pwd or pwd == ''):
				d = xbmcgui.Dialog()
				d.ok('Welcome to fastpasstv.com', 'To start using this plugin first go to the fastpasstv.com.','and register an (free) account.')
				fpt.openSettings(sys.argv[ 0 ]) 
						
params=get_params()
url=None
name=None
mode=None

check_settings()
uname = fpt.getSetting('uname')
pwd   = fpt.getSetting('pwd')

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print "categories"
        CATS()
elif mode==1:
        print "PAGE"
        MOVALL(url,name)
elif mode==2:
        print "PAGE"
        X2(url,name)
elif mode==3:
        print "PAGE"
        X3(url,name)
elif mode==4:
        print "PAGE"
        Y1(url,name)
elif mode==5:
        print "PAGE"
        Y2(url,name)
elif mode==6:
        print "PAGE"
        Y3MOV(url,name)
elif mode==7:
        print "PAGE"
        WOOT(url,name)
elif mode==8:
        print "PAGE"
        VIDSDIVX(url,name)
elif mode==27:
        print "PAGE"
        VIDXFLV(url,name)
elif mode==9:
        print "SEARCH  :"+url
        SEARCH()
elif mode==10:
        print "PAGE"
        VIDBUX(url,name)
elif mode==11:
        print "PAGE"
        ICE(url,name)
elif mode==12:
        print "PAGE"
        Nova(url,name)
elif mode==14:
        print "PAGE"
        NEWEP(url,name)
elif mode==15:
        print "PAGE"
        Mega(url,name)
elif mode==18:
        print "PAGE"
        Y3TV(url,name)
elif mode==19:
        print "PAGE"
        WISE(url,name)
elif mode==20:
        print "PAGE"
        MOVLAT(url,name)
elif mode==21:
        print "PAGE"
        Y3(url,name)
elif mode==22:
        print "PAGE"
        DOCLAT(url,name)
elif mode==23:
        print "PAGE"
        PUTLOC(url,name)
elif mode==24:
        print "PAGE"
        APEX(url,name)
elif mode==25:
        print "PAGE"
        VIDBUX2(url,name)
elif mode==26:
        print "PAGE"
        WOOTAVI(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))