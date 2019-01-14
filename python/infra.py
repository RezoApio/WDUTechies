# Script de merge des fichiers infra.
# test ln windows

import os, time
import re

__DEBUG__ = True

def log(text: str):
    if __DEBUG__:
        print(text)

def get_column(what: str, header: [str], ligne: [str]) -> str:
    assert len(header) >= len(ligne), "La ligne est trop grande"
    log('What:'+what)
    log('Header:'+str(header))
    log('Ligne:'+str(ligne))

    for i in range(len(ligne)):
        if what == header[i]:
            if what == 'Name':
                return ligne[i].lower()
            else:
                return ligne[i]

    return 'N/A'

#Current folder from where to run the .py file (<> from where .py file is located)
PATH=os.getcwd()

OUTPUT='Infra_'+time.strftime("%Y%m%d%H%M")+'.csv'
log(OUTPUT)
COLONNES=['Name', 'State', 'Host', 'Provisioned', 'Host CPU - MHz','Host Mem - MB', 'Guest OS', 'Memory Size', 'CPU Count','From']
#From column will take name of the file
BOM='\ufeff'
NONPROD = re.compile(r"-pp|-rci|-dev|-poc|-prp|-pp|-tpl")
EXPECTEDFILE =  re.compile(r"HDS.*csv|INFRA.*csv|PKI.*csv|PRD.*csv")

output_list = []
sorted_list = []

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #output_list.append(';'.join(COLONNES))
    #log(output_list)
    #Not needed here as we need to sort befoe adding headers
    for name in os.listdir(PATH):

        if not EXPECTEDFILE.search(name):
            log('Non Prod Match')
            continue 
            #Skipping files not expected

        fullname=PATH+"/"+ name
        log(fullname)
        FROM=name[:name.find('.')]
        log(FROM)
        
        with open(fullname,mode='r', encoding='utf-8') as f:
            text=f.read()
            if text.startswith(BOM):
                text =  text[1:]
            
            lines=text.splitlines()
            header=lines[0]
            lines= lines[1:]

            entete=header.split(';')

            for index in range(len(lines)):
                columns=lines[index].split(';')
                if get_column('State', entete, columns) == 'Powered Off':
                    log('Powered Off machine')
                    continue #We do not want powered Off lines
                
                log('NAME::'+ get_column('Name', entete, columns))

                if NONPROD.search(get_column('Name', entete, columns)):
                    log('Non Prod Match')
                    continue #Only Production server

                temp = []
                log(columns)
                for j in range(len(COLONNES)-1): #From will come TYPE variable
                    temp.append(get_column(COLONNES[j], entete, columns))
                    log(temp)
                temp.append(FROM)
                log('On ajoute::' + ';'.join(temp))
                output_list.append(';'.join(temp))

        #This is where I work

        ##file.close()

    #sorted_list.append(';'.join(COLONNES))
    #log(output_list)
    sorted_list = sorted(output_list, key=lambda x: x.split(';',1)[0])
    sorted_list.insert(0,';'.join(COLONNES))
    log(sorted_list)


    sortie = open(PATH+"/"+ OUTPUT, "w")
    sortie.write('\n'.join(sorted_list))
    sortie.close()

    log('\n'.join(sorted_list))

    log("Fini mon kiki")