#!python3
#CodeforcesFileAutomation to create files to reduce time consumption during competetion

import sys , os , requests , webbrowser , bs4 , shutil

print("Creating Files")

os.chdir("C:\\Projects")

userinput = sys.argv[1:]

re = requests.get("".join(userinput))

link_content = userinput[0].split('/')
problem_site = userinput[0][:31] + link_content[-1] + "/problem"

# print(link_content)

folder_title = link_content[3] + " " + link_content[4]
try:
    os.makedirs("C:\\Projects\\" + folder_title)
except:
    pass

re = re.text
soup = bs4.BeautifulSoup(re , 'lxml')

problems = soup.find('table' , class_ = 'problems')
problem_titles = problems.find_all('td' , class_ = 'id')

for names in problem_titles:
    k = names.a['href'].split("/")
    try:
        os.makedirs("C:\\Projects\\" + folder_title + "\\" + k[-2] + " " +  k[-1])
        os.chdir("C:\\Projects\\" + folder_title + "\\" + k[-2] + " " +  k[-1])
        
        shutil.copy("C:\\Projects\\solution.cpp" , os.getcwd())
        inp = open("input.txt" , "w+")
        
        sub_problems = problem_site + "/" + k[-1]
        
        opensprb = requests.get(sub_problems)
        opensprb = opensprb.text
        subsoup = bs4.BeautifulSoup(opensprb , 'lxml')
        
        input_lines = subsoup.find('div' , class_ = 'input').find('pre')
        # print(input_lines.get_text())
        
        inp.write(input_lines.get_text())
        inp.close()
    except:
        #os.chdir("C:\\Projects\\" + folder_title + "\\" + k[-2] + " " +  k[-1])
        #print(os.getcwd())
        pass
    
print("Files Created")
