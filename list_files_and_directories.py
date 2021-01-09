import os
import getpass
from colorama import Fore, Style
import os.path, time

#setting local current directory and user
location = os.getcwd()
user = getpass.getuser()


def fidir(*new_dir, directory=location):

    if len(new_dir) < 1:
        
        files = os.listdir() 
        file_list = []
        dir_list = []
        for f in files:
            file = f.split('.')
            if len(file) < 2:
                dir_list.append(f)
            else:
                file_list.append(f)
        
        x = ''
        r = ''
        w = ''
        print('Access: \tUser: \t\t   File name: \t\t\t\t\t\t File size: \t Created on:')
        print('-'*140)
        for i in file_list:
            if os.access(i, os.R_OK) == True:
                r = 'r'
            else:
                r = '-'
            if os.access(i, os.W_OK) == True:
                w = 'w'
            else:
                w = '-'
            if os.access(i, os.X_OK) == True:
                x = 'x'
            else:
                x = '-'
            size = os.stat(i).st_size
            date = time.ctime(os.path.getctime(i))
            print(Fore.GREEN,'{:<2s}{:<2s}{:<2s}:\t{:^15s}\t\t{:<30s}\t{:>30}\t\t{:>20}'.format(r,w,x,user,i,size,date))
        
        print(Style.RESET_ALL)
        print('')
        print('Access: \tUser: \t\t   Directory name: \t\t\t\t\t File size: \t Created on:')
        print('-'*140)
        for d in dir_list:
            if os.access(d, os.R_OK) == True:
                r = 'r'
            else:
                r = '-'
            if os.access(d, os.W_OK) == True:
                w = 'w'
            else:
                w = '-'
            if os.access(d, os.X_OK) == True:
                x = 'x'
            else:
                x = '-'
            size = os.stat(d).st_size
            date = time.ctime(os.path.getctime(d))
            print(Fore.BLUE,'{:<2s}{:<2s}{:<2s}:\t{:^15s}\t\t{:<30s}\t{:>30}\t\t{:>20}'.format(r,w,x,user,d,size,date),end='')
            print(Style.RESET_ALL)



    if len(new_dir) >= 1:
        
        new_dir = new_dir[0]
        if os.path.exists(str(new_dir)):
            old = new_dir.split('\\')
            splitter = ('\\')
            new = splitter.join(old)
            os.chdir(str(new))
            
            files = os.listdir() 
            file_list = []
            dir_list = []
            for f in files:
                file = f.split('.')
                if len(file) <=1:
                    dir_list.append(f)
                else:
                    file_list.append(f)
                        
            x = ''
            r = ''
            w = ''
            print('Access: \tUser: \t\t   File name: \t\t\t\t\t\t File size: \t Created on:')
            print('-'*140)
            for i in file_list:
                if os.access(i, os.R_OK) == True:
                    r = 'r'
                else:
                    r = '-'
                if os.access(i, os.W_OK) == True:
                    w = 'w'
                else:
                    w = '-'
                if os.access(i, os.X_OK) == True:
                    x = 'x'
                else:
                    x = '-'
                size = os.stat(i).st_size
                date = time.ctime(os.path.getctime(i))
                print(Fore.GREEN,'{:<2s}{:<2s}{:<2s}:\t{:^15s}\t\t{:<30s}\t{:>30}\t\t{:>20}'.format(r,w,x,user,i,size,date))
            
            print(Style.RESET_ALL)
            print('')
            print('Access: \tUser: \t\t   Directory name: \t\t\t\t\t File size: \t Created on:')
            print('-'*140)
                        
            for d in dir_list:
                if os.access(d, os.R_OK) == True:
                    r = 'r'
                else:
                    r = '-'
                if os.access(d, os.W_OK) == True:
                    w = 'w'
                else:
                    w = '-'
                if os.access(d, os.X_OK) == True:
                    x = 'x'
                else:
                    x = '-'
                size = os.stat(d).st_size
                date = time.ctime(os.path.getctime(d))
                print(Fore.BLUE,'{:<2s}{:<2s}{:<2s}:\t{:^15s}\t\t{:<30s}\t{:>30}\t\t{:>20}'.format(r,w,x,user,d,size,date),end='')
                print(Style.RESET_ALL)
      
        elif not os.path.exists(str(new_dir)):
            print('File Directory provided does not exist') 

            

if __name__ == '__main__':
    fidir()
