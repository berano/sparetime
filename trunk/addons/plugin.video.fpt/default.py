import urllib,urllib2,re,sys,xbmcplugin,xbmcgui
import cookielib,os,string,cookielib
import os,time,base64
import xbmcaddon

fpt=xbmcaddon.Addon(id='plugin.video.fpt')

def CATS():
        addDir('Tv Shows','http://www.fastpasstv.com/tv',2,'')
        addDir('New Episodes Added','http://www.fastpasstv.com/tv',14,'')
        addDir('Latest Added Tv Shows','http://www.fastpasstv.com/',4,'')
        addDir('Latest Added Movies','http://www.fastpasstv.com/',5,'')
	addDir('Movies','http://www.fastpasstv.com/movies',1,'')
	addDir('Documentaries','http://www.fastpasstv.com/documentaries',1,'')
	addDir('Cartoons','http://www.fastpasstv.com/cartoons',1,'')
	#addDir('ANIME','http://www.fastpasstv.com/anime',1,'')
	addDir('Search','http://www.fastpasstv.com/',9,'')

def NEWEP(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
     	listnew=re.compile('<li><a href="(.+?)">(.+?)<font class="newvid">New Episodes!').findall(link)
	for url,name in listnew:
		addDir(name+' (NEW EPISODE!)','http://www.fastpasstv.com'+url,4,'http://i42.tinypic.com/iqk4mq.jpg')

def X1(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
     	mvs=re.compile('<li><a href="(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(link)
	for url,name in mvs:
		addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com'+url,6,'')

def X2(url,name): 
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
     	list=re.compile('<li><a href="(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(link)
	for url,name in list:
		addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com'+url,4,'')

def X3(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        link=response2.read()
        response2.close()
      	mvs=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
	for url,name in mvs:
		addDir(name,'http://www.fastpasstv.com'+url,18,'')

def Y1(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
      	tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)</a></li>').findall(link)
      	crt=re.compile('<li><a href="/cartoons/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in tvs:
		addDir(name,'http://www.fastpasstv.com/tv/'+url2,18,'')
	for url2,name in crt:
		addDir(name,'http://www.fastpasstv.com/cartoons/'+url2,18,'')

def Y2(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
      	mvs=re.compile('<li><a href="/movies/(.+?)">(.+?)</a></li>').findall(link)
	for url2,name in mvs:
		addDir(name,'http://www.fastpasstv.com/movies/'+url2,6,'')

def Y3MOV(url,name):

        		req = urllib2.Request(url)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		response2 = urllib2.urlopen(req)
        		ref=response2.geturl()
        		link=response2.read()
       			fv=re.compile('<b>.+?Flash.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
       			fv2=re.compile('<b>.+?FLV.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			dv=re.compile('<b>.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      			dv1=re.compile('<b>.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      			dv2=re.compile('<b>.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      			ml=re.compile('<b>miloyski.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			vz=re.compile('<b>Voez</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			gb=re.compile('<b>.+?hosting.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			meta=re.compile('<b>metadivx.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			gbu=re.compile('<b>gigabyteupload.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			loom=re.compile('<b>loombo.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			dvxlnk=re.compile('<b>divxlink.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      			wise=re.compile('<b>WiseVid</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
			for url in fv:
				addDir('Play (flv) from DivxDen '+'--'+ref,'http://www.fastpasstv.com'+url,7,'','')
			for url in fv2:
				addDir('Play (flv) from DivxDen '+'--'+ref,'http://www.fastpasstv.com'+url,7,'','')
			for url in dv1:
				addDir('Play (avi) from DivxDen (Pt 1) '+'--'+ref,'http://www.fastpasstv.com'+url,8,'','')
			for url in dv2:
				addDir('Play (avi) from DivxDen (Pt 2) '+'--'+ref,'http://www.fastpasstv.com'+url,8,'','')
			for url in dv:
				addDir('Play (avi) from DivxDen '+'--'+ref,'http://www.fastpasstv.com'+url,8,'','')
			for url in wise:
				addDir('Play from wisevid '+ref,'http://www.fastpasstv.com'+url,19,'')

def Y3TV(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response2 = urllib2.urlopen(req)
        ref=response2.geturl()
        link=response2.read()
       	fv=re.compile('<b>.+?Flash.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	dv=re.compile('<b>.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">Watch This Video!').findall(link)
      	dv1=re.compile('<b>.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)" target="_blank">1</a>&nbsp;<a href=".+?"').findall(link)
      	dv2=re.compile('<b>.+?DivX.+?</b></td>\n<td class="siteparts" style="width:.+?px;"><a href=".+?" target="_blank">1</a>&nbsp;<a href="(.+?)"').findall(link)
      	ml=re.compile('<b>miloyski.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	vz=re.compile('<b>Voez</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	gb=re.compile('<b>.+?hosting.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	meta=re.compile('<b>metadivx.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	gbu=re.compile('<b>gigabyteupload.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	loom=re.compile('<b>loombo.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	dvxlnk=re.compile('<b>divxlink.com</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
      	wise=re.compile('<b>WiseVid</b></td>\n<td class="siteparts" style="width:.+?px;"><a href="(.+?)"').findall(link)
	for url in fv:
		addDir('Play (flv) from DivxDen '+'--'+ref,'http://www.fastpasstv.com'+url,7,'')
	for url in dv1:
		addDir('Play (avi) from DivxDen (Pt 1) '+'--'+ref,'http://www.fastpasstv.com'+url,8,'')
	for url in dv2:
		addDir('Play (avi) from DivxDen (Pt 2) '+'--'+ref,'http://www.fastpasstv.com'+url,8,'')
	for url in dv:
		addDir('Play (avi) from DivxDen '+'--'+ref,'http://www.fastpasstv.com'+url,8,'')
	for url in wise:
		addDir('Play from wise '+ref,'http://www.fastpasstv.com'+url,19,'')

def VIDSFLV(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
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
	
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()
	refer=name.replace('Watch This Video @','')

    	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()
	fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link2)[0]
	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link2)[0]

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(gurl, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("s(.+?)182|file").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-46:].replace(' ','')	
	hashshort =  re.compile('divxden(.+?)file').findall(link)[0]
    	finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:182/d/'+hashlong+'/'+ fcodenm
	addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')

def VIDSDIVX(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
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

        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()
	refer=name.replace('Watch This Video @','')

      	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()
	fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link2)[0]
	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link2)[0]

	values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : refer, 'method_free':'Continue to Video'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(gurl, data, headers)
	response = urllib2.urlopen(req)
	link = response.read()

	file=re.compile("custommode(.+?)182").findall(link)[0]
	cleanup=file.replace('|',' ').replace('||',' ')
	hashlong = cleanup[-46:].replace(' ','')
	rawhashshort = re.compile('divxden(.+?)np_vid').findall(link)[0]
	hashshort =  re.compile('divxden(.+?)src').findall(link)[0]
   	finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:182/d/'+hashlong+'/'+ fcodenm
	addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')


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
                req = urllib2.Request('http://www.fastpasstv.com/search',data,headers)
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req).read()
     		tvs=re.compile('<li><a href="/tv/(.+?)">(.+?)<span class="epnum">.+?</span></a></li>').findall(response)
     		docs=re.compile('li><a href="/documentaries/(.+?)">(.+?)<span class="epnum"').findall(response)
     		ctn=re.compile('<li><a href="/cartoons/(.+?)">(.+?)<span class="epnum">.+?</span></a>').findall(response)
     		mvs=re.compile('<li><a href="/movies/(.+?)">(.+?)<span class="epnum">.+?</span></a>').findall(response)
		for url,name in tvs:
			addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com/tv/'+url,4,'')
		for url,name in ctn:
			addDir(name.replace('<font class="newvid">New Episodes!</font>','(NEW EPISODE)'),'http://www.fastpasstv.com/cartoons/'+url,4,'')
		for url,name in mvs:
			addDir(name,'http://www.fastpasstv.com/movies/'+url,6,'')
		for url,name in docs:
			addDir(name,'http://www.fastpasstv.com/documentaries/'+url,6,'')

def WISE(url,name):
	urlogin = 'http://www.fastpasstv.com/register'
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
	#Redirect
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        gurl=response.geturl()

      	req = urllib2.Request(gurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()

	try:
			rawcode=re.compile("javascript:location.href='(.+?)'").findall(link2)[1]
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
			print match
			clean= match.replace("('","")
			finalurl=base64.decodestring(clean)
			addLink('Play',finalurl,'','','')
	except: pass

	try:
			acode=re.compile('<input type="hidden" name="a" value="(.+?)" />').findall(link2)[0]
			vcode=re.compile('<input type="hidden" name="v" value="(.+?)" />').findall(link2)[0]
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
			addLink('Play',finalurl,'','','')
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

def addLink(name,url,iconimage,plot,date):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setInfo( type="Video", infoLabels={ "Plot": plot} )
        liz.setInfo( type="Video", infoLabels={ "Date": date} )
	liz.setProperty("IsPlayable","true");
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok

def check_settings():
		uname = fpt.getSetting('uname')
		pwd   = fpt.getSetting('pwd')
		if (not uname or uname == '') or (not pwd or pwd == ''):
				d = xbmcgui.Dialog()
				d.ok('Welcome to fastpasstv.com', 'To start using this plugin first go to www.fastpasstv.com.','and create an (free) account.')
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
        X1(url,name)
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
        VIDSFLV(url,name)
elif mode==8:
        print "PAGE"
        VIDSDIVX(url,name)
elif mode==9:
        print "SEARCH  :"+url
        SEARCH()
elif mode==10:
        print "PAGE"
        VIDML(url,name)
elif mode==11:
        print "PAGE"
        VIDVZ(url,name)
elif mode==12:
        print "PAGE"
        VID2G(url,name)
elif mode==13:
        print "PAGE"
        VIDGBU(url,name)
elif mode==14:
        print "PAGE"
        NEWEP(url,name)
elif mode==15:
        print "PAGE"
        META(url,name)
elif mode==16:
        print "PAGE"
        LOOM(url,name)
elif mode==17:
        print "PAGE"
        DIVXLINK(url,name)
elif mode==18:
        print "PAGE"
        Y3TV(url,name)
elif mode==19:
        print "PAGE"
        WISE(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))