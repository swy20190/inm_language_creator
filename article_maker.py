import sys
from numpy import random




def article_create(out,notion,concate,idiom,tit,number):
	notion_list=notion.readlines()
	concate_list=concate.readlines()
	idiom_list=idiom.readlines()
	
	result=tit+'\n'
	notion_flag=0
	
	while len(result)<number:
		seed=random.randn()
		if seed<-2:
			result=result+tit
			notion_flag=1
		elif seed<-1 and notion_flag==1:
			nseed=random.randint(0,len(notion_list))
			curr_n=notion_list[nseed]
			result=result+curr_n
			notion_flag=0
		elif seed<1:
			iseed=random.randint(0,len(idiom_list))
			curr_i=idiom_list[iseed]
			result=result+curr_i
			notion_flag=1
		elif seed<2:
			cseed=random.randint(0,len(concate_list))
			curr_c=concate_list[cseed]
			result=result+curr_c
			notion_flag=1
		elif seed<3:
			result+='\n'
			notion_flag=0
	
	out.write(result)
def main(argv):			
	word_num=int(argv[1])
	title=argv[2]
	try:		
		article_obj=open('output.txt','wt')
		try:
			notions_obj=open('notions.txt','rt')
			try:
				concate_obj=open('concate.txt','rt')
				try:
					idioms_obj=open('idioms.txt','rt')
					article_create(article_obj,notions_obj,concate_obj,idioms_obj,title,word_num)
					idioms_obj.close()
				except Exception as err:
					print(err)
			
				concate_obj.close()
			except Exception as err:
				print(err)
		
			notions_obj.close()
		except Exception as err:
			print(err)
		article_obj.close()

	except Exception as err:
		print(err)

if __name__=="__main__":
	main(sys.argv)
