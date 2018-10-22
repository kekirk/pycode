#!/usr/bin/python
# coding: utf-8
#批量解压日志程序
#writen by 刘泽群

#(导入模块使用:包括时间管理模块，系统命令模块，日志输出模块，异常信息获取模块，等等)

import datetime
import time
import os
import sys
import logging
import logging.config
import logging.handlers
import traceback
import progressbar

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
"[%(asctime)s %(filename)s:%(lineno)s - %(funcName)15s()] %(message)s"
)
#日志输出位置，到指定/hskj/logs/piliang_tar.log这个文件，从系统规划上，日志统一放置到这个地方
handler = logging.handlers.RotatingFileHandler("/hskj/logs/piliang_tar.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

#配置格式化信息输出
public_log_txt="/hskj/script/python_tar/data_txt/riz.log"

#功能调用这块同一通过类方法来实现。
class Wjlist():

#实现打开集群功能信息文件，按照标号选择集群
    def wenjian(self,list_dir):
        with open(list_dir) as f:
             content = f.read()
             print content

#通过序号，来选择执行主机的路径功能（用于解压功能具体实现）
    def wenjian_list(self,wj_lj,xuhao):
        with open(wj_lj) as fp:
             config = fp.read().split('\n')
             if xuhao==1:
                     w1hang=config[0]
                     w1=w1hang.split(" ")
                     global sb_01
                     sb_01=w1[1]

             elif xuhao==2:
                     w2hang=config[1]
                     w2=w2hang.split(" ")
                     global sb_02
                     sb_02=w2[1]
 
             elif xuhao==3:
                     w3hang=config[2]
                     w3=w3hang.split(" ")
                     global sb_03
                     sb_03=w3[1]

             elif xuhao==4:
                     w4hang=config[3]
                     w4=w4hang.split(" ")
                     global sb_04
                     sb_04=w4[1]

             elif xuhao==5:
                     w5hang=config[4]
                     w5=w5hang.split(" ")
                     global sb_05
                     sb_05=w5[1]   
      
             elif xuhao==6:
                     w6hang=config[5]
                     w6=w6hang.split(" ")
                     global sb_06
                     sb_06=w6[1]

             elif xuhao==7:
                     w7hang=config[6]
                     w7=w7hang.split(" ")
                     global sb_07
                     sb_07=w7[1]

             elif xuhao==8:
                     w8hang=config[7]
                     w8=w8hang.split(" ")
                     global sb_08
                     sb_08=w8[1]

             elif xuhao==9:
                     w9hang=config[8]
                     w9=w9hang.split(" ")
                     global sb_09
                     sb_09=w9[1]

             elif xuhao==10:
                     w10hang=config[9]
                     w10=w10hang.split(" ")
                     global sb_10
                     sb_10=w10[1]

             elif xuhao==11:
                     w11hang=config[10]
                     w11=w11hang.split(" ")
                     global sb_11
                     sb_11=w11[1]

             elif xuhao==12:
                     w12hang=config[11]
                     w12=w12hang.split(" ")
                     global sb_12
                     sb_12=w12[1]

             elif xuhao==13:
                     w13hang=config[12]
                     w13=w13hang.split(" ")
                     global sb_13
                     sb_13=w13[1]

             elif xuhao==14:
                     w14hang=config[13]
                     w14=w14hang.split(" ")
                     global sb_14
                     sb_14=w14[1]

             elif xuhao==15:
                     w15hang=config[14]
                     w15=w15hang.split(" ")
                     global sb_15
                     sb_15=w15[1]

             elif xuhao==16:
                     w16hang=config[15]
                     w16=w16hang.split(" ")
                     global sb_16
                     sb_16=w16[1]

             elif xuhao==17:
                     w17hang=config[16]
                     w17=w17hang.split(" ")
                     global sb_17
                     sb_17=w17[1]
#针对该集群下，有那些主机日志文件
    def bl_list(self,path):
	     try:
                 clear_nr="cat /dev/null >"+public_log_txt
                 os.system(clear_nr)
                 for root,dirs,files in os.walk(path):
                           with open(public_log_txt,'a+') as f:
                                   printcipal = root
                                   print >> f,"%s"% printcipal
                 minl="cat "+public_log_txt+"|sort" 
                 os.system(minl)   
				 
             except:
                 logger.exception(traceback.print_exc())
                 exit()
    

#只选择针对.tar.gz的文件进行过滤
    def bl_wj(self,path):
	     try:
                 dizh=path
                 items=os.listdir(path)
                 global newlist
                 newlist = []
                 for names in items:
                     if names.endswith('.tar.gz'):
                         newlist.append(names)
						 
             except:
                 logger.exception(traceback.print_exc())
                 exit()
   
#具体解压任务执行方法
    def tar_list(self,baowj):
                 mima='"&U*I(O707"'
                 for i in baowj:
	                try:
                            os.system('mkdir -p /hskj/tmp/wj_nr')
                            os.chdir('/hskj/tmp/wj_nr') 
                            np=i.split("/")
                            wjj="mkdir -p "+np[4]
                            os.system(wjj)
                            os.chdir(np[4])
                            jieya="openssl enc -des -d -a -in "+i+" -k "+mima+"| tar -zx "
                            print "文件解压名称：%s" % i
                            os.system(jieya) 
                            p = progressbar.ProgressBar()
                            N = 500
                            for i in p(range(N)):
                                time.sleep(0.01)
						   
			except:
                            logger.exception(traceback.print_exc())
                            exit()
			  

    def tar_data_list(self,baowj):
                 mima='"&U*I(O707"'
                 for i in baowj:
                        try:
                            os.system('mkdir -p /hskj/tmp/wj_nr')
                            os.chdir('/hskj/tmp/wj_nr')
                            np=i.split("/")
                            wjj="mkdir -p "+np[4]
                            os.system(wjj)
                            os.chdir(np[4])
                            tb_n=np[5]
                            tb_nn=tb_n.split(".")
                            print "解压文件 %s" % np[4]
                            single_table=raw_input("请写入你要解压的具体表名:").lstrip()
                            jieya="openssl enc -des -d -a -in "+i+" -k "+mima+"| tar -zx "+tb_nn[0]+"/"+single_table+"*"+" &"
                            print "文件解压名称：%s" % i
#                            def shuchulist():
#                                   p = progressbar.ProgressBar()
#                                   N = 1000
#                                   for i in p(range(N)):
#                                       time.sleep(0.02)
                            os.system(jieya)                         
                        except:
                            logger.exception(traceback.print_exc())
                            exit()

public_dir="/hskj/script/python_tar/data_txt"
quanlist=Wjlist()
quanlist.wenjian(public_dir+"/"+"host_team")
num_hao=int(raw_input("请选择你要进入的集群(序号):"))
print num_hao
global kou
kou=[]
while True:
#针对数北集群处理的任务
      if num_hao == 1:
             shubei=Wjlist()
             shubei.wenjian(public_dir+"/"+"shubei.txt")
             cluster_name=int(raw_input("请选择你要进入的主机名(序号):"))
             if cluster_name == 1:
                      cs1=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",1)
                      cs1=shubei.bl_list(sb_01)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_01+"/"+wj
                      cs1=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 2:
                      cs2=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",2)
                      cs2=shubei.bl_list(sb_02)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_02+"/"+wj                       
                      cs2=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 3:
                      cs3=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",3)
                      cs3=shubei.bl_list(sb_03)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_03+"/"+wj
                      cs3=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 4:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",4)
                      cs4=shubei.bl_list(sb_04)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_04+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 5:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",5)
                      cs4=shubei.bl_list(sb_05)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_05+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 6:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",6)
                      cs4=shubei.bl_list(sb_06)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_06+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 7:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",7)
                      cs4=shubei.bl_list(sb_07)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_07+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 8:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",8)
                      cs4=shubei.bl_list(sb_08)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_08+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 9:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",9)
                      cs4=shubei.bl_list(sb_09)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_09+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 10:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",10)
                      cs4=shubei.bl_list(sb_10)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_10+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 11:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",11)
                      cs4=shubei.bl_list(sb_11)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_11+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 12:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",12)
                      cs4=shubei.bl_list(sb_12)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_12+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 13:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",13)
                      cs4=shubei.bl_list(sb_13)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_13+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 14:
                      cs4=shubei.wenjian_list(public_dir+"/"+"shubei_gn.txt",14)
                      cs4=shubei.bl_list(sb_14)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_14+"/"+wj
                      cs4=shubei.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 99:
                      zhxing=shubei.tar_list(kou)


             elif cluster_name == 88: 
                      break              

#针对三元桥集群处理的任务            
      elif num_hao == 2:             
             sanyq=Wjlist()
             sanyq.wenjian(public_dir+"/"+"sanyq.txt")
             cluster_name=int(raw_input("请选择你要进入的主机名:"))
             if cluster_name == 1:
                      cs1=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",1)
                      cs1=sanyq.bl_list(sb_01)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_01+"/"+wj
                      cs1=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 2:
                      cs2=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",2)
                      cs2=sanyq.bl_list(sb_02)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_02+"/"+wj                       
                      cs2=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 3:
                      cs3=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",3)
                      cs3=sanyq.bl_list(sb_03)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_03+"/"+wj
                      cs3=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 4:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",4)
                      cs4=sanyq.bl_list(sb_04)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_04+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 5:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",5)
                      cs4=sanyq.bl_list(sb_05)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_05+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 6:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",6)
                      cs4=sanyq.bl_list(sb_06)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_06+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 7:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",7)
                      cs4=sanyq.bl_list(sb_07)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_07+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 8:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",8)
                      cs4=sanyq.bl_list(sb_08)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_08+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 9:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",9)
                      cs4=sanyq.bl_list(sb_09)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_09+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 10:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",10)
                      cs4=sanyq.bl_list(sb_10)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_10+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 11:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",11)
                      cs4=sanyq.bl_list(sb_11)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_11+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 12:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",12)
                      cs4=sanyq.bl_list(sb_12)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_12+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 13:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",13)
                      cs4=sanyq.bl_list(sb_13)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_13+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 14:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",14)
                      cs4=sanyq.bl_list(sb_14)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_14+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 15:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",15)
                      cs4=sanyq.bl_list(sb_15)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_15+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 16:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",16)
                      cs4=sanyq.bl_list(sb_16)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_16+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 17:
                      cs4=sanyq.wenjian_list(public_dir+"/"+"sanyq_gn.txt",17)
                      cs4=sanyq.bl_list(sb_17)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_17+"/"+wj
                      cs4=sanyq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 99:
                      zhxing=sanyq.tar_list(kou)

#针对马驹桥集群处理的任务					  
      elif num_hao == 3:
             majq=Wjlist()
             majq.wenjian(public_dir+"/"+"majq.txt")
             cluster_name=int(raw_input("请选择你要进入的主机名(序号):"))
             if cluster_name == 1:
                      cs1=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",1)
                      cs1=majq.bl_list(sb_01)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_01+"/"+wj
                      cs1=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      print mingcheng
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 2:
                      cs2=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",2)
                      cs2=majq.bl_list(sb_02)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_02+"/"+wj                       
                      cs2=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 3:
                      cs3=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",3)
                      cs3=majq.bl_list(sb_03)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_03+"/"+wj
                      cs3=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 4:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",4)
                      cs4=majq.bl_list(sb_04)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_04+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 5:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",5)
                      cs4=majq.bl_list(sb_05)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_05+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 6:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",6)
                      cs4=majq.bl_list(sb_06)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_06+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 7:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",7)
                      cs4=majq.bl_list(sb_07)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_07+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 8:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",8)
                      cs4=majq.bl_list(sb_08)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_08+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 9:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",9)
                      cs4=majq.bl_list(sb_09)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_09+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 10:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",10)
                      cs4=majq.bl_list(sb_10)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_10+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 11:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",11)
                      cs4=majq.bl_list(sb_11)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_11+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 12:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",12)
                      cs4=majq.bl_list(sb_12)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_12+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 13:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",13)
                      cs4=majq.bl_list(sb_13)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_13+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 14:
                      cs4=majq.wenjian_list(public_dir+"/"+"majq_gn.txt",14)
                      cs4=majq.bl_list(sb_14)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_14+"/"+wj
                      cs4=majq.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 99:
                      zhxing=majq.tar_list(kou)

             elif cluster_name == 88:
                      break
					  
#针对沙河移动集群处理的任务
      elif num_hao == 4:
             shahyd=Wjlist()
             shahyd.wenjian(public_dir+"/"+"shahyd.txt")
             cluster_name=int(raw_input("请选择你要进入的主机名(序号):"))
             if cluster_name == 1:
                      cs1=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",1)
                      cs1=shahyd.bl_list(sb_01)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_01+"/"+wj
                      cs1=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 2:
                      cs2=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",2)
                      cs2=shahyd.bl_list(sb_02)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_02+"/"+wj                       
                      cs2=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 3:
                      cs3=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",3)
                      cs3=shahyd.bl_list(sb_03)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_03+"/"+wj
                      cs3=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 4:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",4)
                      cs4=shahyd.bl_list(sb_04)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_04+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 5:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",5)
                      cs4=shahyd.bl_list(sb_05)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_05+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 6:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",6)
                      cs4=shahyd.bl_list(sb_06)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_06+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 7:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",7)
                      cs4=shahyd.bl_list(sb_07)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_07+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 8:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",8)
                      cs4=shahyd.bl_list(sb_08)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_08+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 9:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",9)
                      cs4=shahyd.bl_list(sb_09)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_09+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 10:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",10)
                      cs4=shahyd.bl_list(sb_10)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_10+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 11:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",11)
                      cs4=shahyd.bl_list(sb_11)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_11+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 12:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",12)
                      cs4=shahyd.bl_list(sb_12)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_12+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 13:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",13)
                      cs4=shahyd.bl_list(sb_13)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_13+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 14:
                      cs4=shahyd.wenjian_list(public_dir+"/"+"shahyd_gn.txt",14)
                      cs4=shahyd.bl_list(sb_14)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_14+"/"+wj
                      cs4=shahyd.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 99:
                      zhxing=shahyd.tar_list(kou)

             elif cluster_name == 88:
                      break

#针对上海电信集群处理的任务
      elif num_hao == 5:
             shanghdx=Wjlist()
             shanghdx.wenjian(public_dir+"/"+"shanghdx.txt")
             cluster_name=int(raw_input("请选择你要进入的主机名(序号):"))
             if cluster_name == 1:
                      cs1=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",1)
                      cs1=shanghdx.bl_list(sb_01)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_01+"/"+wj
                      cs1=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 2:
                      cs2=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",2)
                      cs2=shanghdx.bl_list(sb_02)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_02+"/"+wj                       
                      cs2=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 3:
                      cs3=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",3)
                      cs3=shanghdx.bl_list(sb_03)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_03+"/"+wj
                      cs3=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 4:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",4)
                      cs4=shanghdx.bl_list(sb_04)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_04+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 5:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",5)
                      cs4=shanghdx.bl_list(sb_05)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_05+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 6:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",6)
                      cs4=shanghdx.bl_list(sb_06)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_06+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 7:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",7)
                      cs4=shanghdx.bl_list(sb_07)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_07+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 8:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",8)
                      cs4=shanghdx.bl_list(sb_08)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_08+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 9:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",9)
                      cs4=shanghdx.bl_list(sb_09)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_09+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue


             elif cluster_name == 10:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",10)
                      cs4=shanghdx.bl_list(sb_10)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_10+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 11:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",11)
                      cs4=shanghdx.bl_list(sb_11)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_11+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 12:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",12)
                      cs4=shanghdx.bl_list(sb_11)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_11+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 13:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",13)
                      cs4=shanghdx.bl_list(sb_13)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_13+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 14:
                      cs4=shanghdx.wenjian_list(public_dir+"/"+"shanghdx_gn.txt",14)
                      cs4=shanghdx.bl_list(sb_14)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_14+"/"+wj
                      cs4=shanghdx.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 99:
                      zhxing=shanghdx.tar_list(kou)

             elif cluster_name == 88:
                      break
                  
#数据库主机解压组
      elif num_hao == 13:
             shujuku=Wjlist()
             shujuku.wenjian(public_dir+"/"+"jiqun_database_host.txt")
             cluster_name=int(raw_input("请选择你要进入的主机名(序号):"))
             if cluster_name == 1:
                      cs1=shujuku.wenjian_list(public_dir+"/"+"jiqun_database.txt",1)
                      cs1=shujuku.bl_list(sb_01)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_01+"/"+wj
                      cs1=shujuku.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             if cluster_name == 2:
                      cs1=shujuku.wenjian_list(public_dir+"/"+"jiqun_database.txt",2)
                      cs1=shujuku.bl_list(sb_02)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_02+"/"+wj
                      cs1=shujuku.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             if cluster_name == 3:
                      cs1=shujuku.wenjian_list(public_dir+"/"+"jiqun_database.txt",3)
                      cs1=shujuku.bl_list(sb_03)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_03+"/"+wj
                      cs1=shujuku.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             if cluster_name == 4:
                      cs1=shujuku.wenjian_list(public_dir+"/"+"jiqun_database.txt",4)
                      cs1=shujuku.bl_list(sb_04)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_04+"/"+wj
                      cs1=shujuku.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             if cluster_name == 5:
                      cs1=shujuku.wenjian_list(public_dir+"/"+"jiqun_database.txt",5)
                      cs1=shujuku.bl_list(sb_05)
                      wj=raw_input("清选择你要进入的文件名 格式:(主机名-年-月-日):").lstrip()
                      lujing=sb_05+"/"+wj
                      cs1=shujuku.bl_wj(lujing)
                      mingcheng=lujing+"/"+str(newlist[0])
                      kou.append(mingcheng)
                      print kou
                      continue

             elif cluster_name == 99:
                      zhxing=shujuku.tar_data_list(kou)

             elif cluster_name == 88:
                      break

      else:
             print "nothing is null"
             num_hao=int(raw_input("请选择你要进入的集群:")) 
             continue
