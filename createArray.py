from sys import argv
from os import system
from os import getlogin


class CreateArray(object):

    def __init__(self) -> None:
        """
            TODO When --break valuer is greate that array size, the break create one array (Need fix it)
        """
        self.debug = True
        self.arguments = self.get_user_arguments()
        self.split_array = False
        self.separetor_custom = False
        self.split_array_valuer = 0
        self.separetor_valuer = ','
        self.path_output_file = f'C:\\Users\\{getlogin()}\\Desktop\\saidaArray.txt'
        self.array_to_transform = list()
        self.check_default_arguments()  # Check arguments and default arguments
        self.init_arguments_rules() # This fuction is vary important to help in the default arguments (Check and fix valuers)
        self.user_array_size = self.get_total_element_in_array()

        # Attributes comming with parameters

        self.array_user_data = [element.strip() for element in self.arguments[-1].split(self.separetor_valuer)] # Split string array send by user in terminal
        


    


    def check_default_arguments(self):
        """
            Check default argument with user send by terminal.
        """
        # Frist step check with the array argument has been send
        if not self.arguments:
            print('''\nERRO: Necessario enviar dados string por parametro!
                Exemplo de uso:
                Exemplo 1: createArray.py  --break 2 "element01, element02, element03"
                Exemplo 2: createArray.py "element1, element1"\n
                ''')
            exit(0)
        


        # Break rules
        if '--break' in self.arguments: 
            self.split_array = True
        if '--sep' in self.arguments:
            self.separetor_custom = True


    
    def init_arguments_rules(self):
        """
            Define rules for arguments
        """

        if self.split_array: # Rules for break array
            try:
                self.split_array_valuer = int(self.arguments[self.arguments.index('--break') + 1])  # Get break valuer send by user in terminal
            except ValueError:
                self.split_array_valuer = 10 # Default valuer for break

            if self.split_array_valuer <= 0:
                print('Negative or "0" valuer for "--break" is not allow, only positive valuers!')
                exit(0)
            elif self.split_array_valuer == 1: # If valuer is equal to 1, create one array.
                self.split_array = False

        if  self.separetor_custom:
            self.separetor_valuer = self.arguments[self.arguments.index('--sep') + 1]


    def init_array_data(self):
        """
            Split array using break valuer user give in the terminal
        """

        # Generate array data with break valuer 0, 4 - 2
        if self.split_array:
            self.array_to_transform = [self.array_user_data[array_valuer:array_valuer + self.split_array_valuer] for array_valuer in range(0, len(self.array_user_data), self.split_array_valuer)]
            print('aaa: ' + str([self.array_user_data[array_valuer:array_valuer + self.split_array_valuer] for array_valuer in range(0, len(self.array_user_data), self.split_array_valuer)]))
        else:
            self.array_to_transform = [element for element in self.array_user_data] # Return one array without break
        

    def write_data_in_output_file(self):
        """
            Write all data in output file txt
        """

        with open(self.path_output_file, 'w') as fileOutput:
            
            if self.split_array:  # If break array
                
                len_data_array = len(self.array_to_transform)
                
                fileOutput.write(f'-=-=-=-=-=-=-= Inicio da geração de Arrays -=-=-=-=-=-=-=\n\n')

                for index, array_element in enumerate(self.array_to_transform):
                    fileOutput.write(f'{index + 1 }º - {array_element}\n\n')
                    #fileOutput.write(str(self.array_to_transform) + '\n')
                fileOutput.write(f'=-=-=-==-=-=--==-= Resultado da geração =-=-=-==-=-=--==-=\n\n')
                fileOutput.writelines(f'Soma de elementos dos Arrays: {self.user_array_size}\n')
                fileOutput.writelines(f'Total de Arrays gerados: {len_data_array}\n')
                    
            else:  # If not break array
                fileOutput.write(f'-=-=-=-=-=-=-= Inicio da geração de Arrays -=-=-=-=-=-=-=\n\n')
                fileOutput.write(f'{self.array_to_transform}\n')
                fileOutput.write(f'=-=-=-==-=-=--==-= Resultado da geração =-=-=-==-=-=--==-=\n\n')
                fileOutput.writelines(f'\nTotal de elementos dentro do Array:{self.user_array_size}\n')
                fileOutput.writelines('Uma array foi gerado apenas\n')
                fileOutput.write('\n\n')
            fileOutput.close()
            
        system('start ' + self.path_output_file)


    def __str__(self):
        """
            To print data output in terminal
        """

        return f'''SEP Active: {self.separetor_custom}
        Sep Valuer: {self.separetor_valuer}\n
        Path User: {self.path_output_file}\n
        Array RAW data: {self.array_user_data }\n
        Arguments comming from terminal: {self.arguments}\n
        break array? {self.split_array}\n
        break array valuer: {self.split_array_valuer}\n
        Array generate by function: {self.array_to_transform}\n
        Split array to write in file: {self.array_to_transform}\n
        '''

    def get_user_arguments(self) -> list:
        return [ x.lower() for x in argv[1:] ] # Exclude frist element in arguments, is program name!

    def get_total_element_in_array(self) -> int:
        return len(self.arguments[-1].split(self.separetor_valuer))

    def run(self):
        """
            Init program
        """
        self.init_array_data()
        self.write_data_in_output_file()



create_array_obj = CreateArray()
create_array_obj.run()