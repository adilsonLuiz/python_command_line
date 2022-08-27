from sys import argv
from os import system
from os import getlogin


class CreateArray(object):

    def __init__(self) -> None:
        self.debug = False
        self.arguments = [ x.lower() for x in argv[1:] ] # Exclude frist element in arguments, is program name!
        self.print_debug(f'Arguments comming from terminal: {self.arguments}')
        self.split_array = False
        self.path_output_file = f'C:\\Users\\{getlogin()}\\Desktop\\saidaArray.txt'
        self.print_debug(f'Path User: {self.path_output_file}')
        self.array_to_transform = list()
        self.total_elements_array_argv = len(self.arguments[-1].split(','))
        self.array_user_data = [element.strip() for element in self.arguments[-1].split(',')] # Split string array send by user in terminal
        self.print_debug(f'Array RAW data: {self.array_user_data }')
        self.split_array_valuer = 0
        self.check_default_arguments()  # Check arguments and default arguments


    def check_default_arguments(self):
        """
            Check default argument with user send by terminal.
        """
        print()
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
            self.print_debug('--break argument find in the arguments!')
            self.split_array = True
            try:
                self.split_array_valuer = int(self.arguments[self.arguments.index('--break') + 1])  # Get break valuer send by user in terminal
            except ValueError:
                self.split_array_valuer = 2

            if self.split_array_valuer <= 0:
                print('Negative or "0" valuer for "--break" is not allow, only positive valuers!')
                exit(0)
            elif self.split_array_valuer == 1: # If valuer is equal to 1, create one array.
                self.split_array = False

        self.print_debug(f'split array is active: {self.split_array}')
        self.print_debug(f'User break valuer type: {self.split_array_valuer}')

    
    def init_array_data(self):
        """
            Split array using break valuer user give in the terminal
        """

        # Generate array data with break valuer 0, 4 - 2
        if self.split_array:
            self.array_to_transform = [self.array_user_data[array_valuer:array_valuer + self.split_array_valuer] for array_valuer in range(0, len(self.array_user_data), self.split_array_valuer)]
        else:
            self.array_to_transform = [element for element in self.array_user_data] # Return one array without break
        
        self.print_debug(f'break array? {self.split_array}')
        self.print_debug(f'Array generate by function: {self.array_to_transform}')


    def write_data_in_output_file(self):
        """
            Write all data in output file txt
        """

        with open(self.path_output_file, 'w') as fileOutput:
            
            if self.split_array:  # If break array
                
                len_data_array = len(self.array_to_transform)
                self.print_debug(f'Split array to write in file: {self.array_to_transform}')
                fileOutput.write(f'-=-=-=-=-=-=-= Inicio da geração de Arrays -=-=-=-=-=-=-=\n\n')

                for index, array_element in enumerate(self.array_to_transform):
                    fileOutput.write(f'{index + 1 }º - {array_element}\n\n')
                    #fileOutput.write(str(self.array_to_transform) + '\n')
                fileOutput.write(f'=-=-=-==-=-=--==-= Resultado da geração =-=-=-==-=-=--==-=\n\n')
                fileOutput.writelines(f'Soma de elementos dos Arrays: {self.total_elements_array_argv}\n')
                fileOutput.writelines(f'Total de Arrays gerados: {len_data_array}\n')
                    
            else:  # If not break array
                fileOutput.write(f'-=-=-=-=-=-=-= Inicio da geração de Arrays -=-=-=-=-=-=-=\n\n')
                fileOutput.write(f'{self.array_to_transform}\n')
            fileOutput.write(f'=-=-=-==-=-=--==-= Resultado da geração =-=-=-==-=-=--==-=\n\n')
            fileOutput.writelines(f'\nTotal de elementos dentro do Array:{str(self.total_elements_array_argv)}\n')
            fileOutput.writelines('Uma array foi gerado apenas\n')
            fileOutput.write('\n\n')
            fileOutput.close()
            
        system('start ' + self.path_output_file)


    def print_debug(self, data):
        """
            To print data output in terminal
        """
        if self.debug:
            print(data)


    def run(self):
        """
            Init program
        """
        self.init_array_data()
        self.write_data_in_output_file()

        pass


create_array_obj = CreateArray()
create_array_obj.run()
