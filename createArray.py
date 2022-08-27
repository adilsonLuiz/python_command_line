from sys import argv
from os import system


class CreateArray(object):
    
    def __init__(self) -> None:
        self.arguments = argv[1:]
        self.path_output_file = 'C:\\Users\\adilsjun\\Desktop\\saidaArray.txt'
        self.total_elements = len(self.arguments[-1].split(','))
        self.data_array_trasform = self.arguments[-1].split(',')# Root argument to trasform em array
        self.breakArray = False
        self.breakArrayValue = 0
        self.check_default_arguments() # Check arguments and default arguments

    def check_default_arguments(self):
        """Trata os argumentos que usuário envia"""
        
        if not self.arguments:
            print('''ERRO: Necessario enviar dados string por parametro!
                    Exemplo de uso:
                    Exemplo 1: createArray.py  --break 2 "element01, element02, element03"
                    Exemplo 2: createArray.py "element1, element1"
                ''')
            exit(0)
        
        if '--break' in self.arguments:
            self.breakArray = True
            self.breakArrayValue = int(self.arguments[self.arguments.index('--break') + 1]) # Get break valuer
            self.data_array_trasform = [self.data_array_trasform[i:i + self.breakArrayValue] \
                 for i in range(0, len(self.data_array_trasform), self.breakArrayValue)] # Generate array data with break valuer
        else: # Generate array data 
            self.data_array_trasform = [ element for element in self.data_array_trasform] # Get all valuer of element without breaking.


    def trasform_array(self):
        """Cria o array baseado no ultimo argumento enviado"""

        with open(self.path_output_file, 'w') as fileOutput:
            if self.breakArray: # If break array
                len_data_array = len(self.data_array_trasform)
                fileOutput.write('\n\n')
                for i in range(0, len_data_array):
                    fileOutput.write(str(self.data_array_trasform[i]) + '\n')
                fileOutput.write(str(self.data_array_trasform) + '\n')
                fileOutput.writelines('Total de elementos: ' + str(self.total_elements) + '\n\n')
                fileOutput.writelines('Total de Arrays gerados: ' + str(len_data_array) + '\n\n')
                fileOutput.write('\n\n')
                fileOutput.close()
            else: # If not break array
                len_data_array = len(self.data_array_trasform)
                fileOutput.write('\n\n')
                fileOutput.write(str(self.data_array_trasform) + '\n')
                fileOutput.writelines(f'''
                \nTotal de elementos dentro do array:{str(self.total_elements)}\n
                Uma array foi gerado apenas\n
                ''')
                fileOutput.write('\n\n')
                fileOutput.write('\n\n')
                fileOutput.close()

        system('start ' + self.path_output_file)



t = CreateArray()
t.trasform_array()




