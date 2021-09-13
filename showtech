import task_iosstp_library
from prettytable import PrettyTable
import logging

logger = logging.getLogger("SIF_ASIC_REGISTERS")
logging.getLogger().setLevel(logging.INFO)

def task(env, showtech1, showtech2):
    
        logger.info("Running as standalone...")
        standalone(showtech1)






def standalone(showtech1):
    
    table = PrettyTable()
    table.field_names = ["Member", "ASIC Register", "Value"]
    
    
    show_tech = task_iosstp_library.IOSPreParsedShowTech(showtech1)
    stack_members = show_tech.get_command("show switch detail")
    
    num_switches = 0
    matches = ["Active", "Standby", "Member"]

    for line in stack_members["lines"]:
        if any(x in line for x in matches):
            num_switches = num_switches + 1
            
    print(num_switches)
    
    for switch_num in range(1, num_switches+1):
        #print("Switch {} SIF Errors".format(switch_num))
        
        crc0 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-0 asic 0 core 0".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-0 asic 0 core 0", crc0["lines"][-2].split(":")[-1] ])
        
        crc1 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-1 asic 0 core 0".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-1 asic 0 core 0", crc1["lines"][-2].split(":")[-1] ])
        
        crc2 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-2 asic 0 core 0".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-2 asic 0 core 0", crc2["lines"][-2].split(":")[-1] ])
        
        crc3 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-3 asic 0 core 0".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-3 asic 0 core 0", crc3["lines"][-2].split(":")[-1] ])
        
        crc4 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-4 asic 0 core 0".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-4 asic 0 core 0", crc4["lines"][-2].split(":")[-1] ])
        
        crc5 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-5 asic 0 core 0".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-5 asic 0 core 0", crc5["lines"][-2].split(":")[-1] ])
        
        crc01 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-0 asic 0 core 1".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-0 asic 0 core 1", crc01["lines"][-2].split(":")[-1] ])
        
        crc11 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-1 asic 0 core 1".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-1 asic 0 core 1", crc11["lines"][-2].split(":")[-1] ])
        
        crc21 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-2 asic 0 core 1".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-2 asic 0 core 1", crc21["lines"][-2].split(":")[-1] ])
        
        crc31 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-3 asic 0 core 1".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-3 asic 0 core 1", crc31["lines"][-2].split(":")[-1] ])
        
        crc41 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-4 asic 0 core 1".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-4 asic 0 core 1", crc41["lines"][-2].split(":")[-1] ])
        
        crc51 = show_tech.get_command("show platform hardware fed switch {} fwd-asic register read register-name SifRacDataCrcErrorCnt-5 asic 0 core 1".format(switch_num))
        table.add_row([switch_num, "SifRacDataCrcErrorCnt-5 asic 0 core 1", crc51["lines"][-2].split(":")[-1] ])
        
    print(table)
    print(show_tech)
    return table
