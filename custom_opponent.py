#python3 custom_opponent.py battle-1.solution PB014 "UNNAMED0.PRJ" 2 ALPHA.exa BETA.exa
#python3 custom_opponent.py battle-1.solution PB014 "TEST" 1 TEST.exa

import struct
import sys
import os

def create_solution_file(output_path, file_name, solution_name, num_programs, programs):
    try:
        with open(output_path, 'wb') as file:
            # Beginning of file
            file.write(b'\xED\x03\x00\x00')
            
            # Header
            file.write(struct.pack('<I', len(file_name)))
            file.write(file_name.encode('utf-8'))
            file.write(struct.pack('<I', len(solution_name)))
            file.write(solution_name.encode('utf-8')) 
            file.write(b'\x00\x00\x00\x00')
            file.write(struct.pack('<I', num_programs))  # Number of programs

            # Programs
            for program_name, program_data in programs:
                file.write(b'\x0A')  # S (repeating pattern for each subsequent program)
                file.write(struct.pack('<I', len(program_name))) 
                file.write(program_name.encode('utf-8'))
                code_length = len(program_data.encode('utf-8')) 
                file.write(struct.pack('<I', code_length))
                file.write(program_data.encode('utf-8'))
                file.write(b'\x00\x00')  # End of program code

        print(f"File {output_path} successfully created.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("All arguments must be specified: [output file name] [file name] [solution name] [number of programs] [names of program files]")
        sys.exit(1)

    output_path = sys.argv[1]
    file_name = sys.argv[2]
    solution_name = sys.argv[3]
    num_programs = int(sys.argv[4])
    
    programs = []
    for i in range(num_programs):
        program_file_name = sys.argv[5 + i]
        with open(program_file_name, 'r', encoding='utf-8') as program_file:
            program_data = program_file.read()
        programs.append((os.path.splitext(program_file_name)[0], program_data))

    create_solution_file(output_path, file_name, solution_name, num_programs, programs)

