
import json , time , argparse , os

class Program():
    parser = argparse.ArgumentParser(description='Program manajemen pemasukan dan pengeluaran')
    parser.add_argument('-f', '--file',type=str, required=True, help="File database")
    parser.add_argument('-i', '--income',type=int, help="Jumlah income pemasukan keuangan")
    parser.add_argument('-o', '--outcome',type=int, help="Jumlah pengeluaran pemasukan")
    parser.add_argument('-d', '--description', required=True,help='Tampilan deskripsi')
    args = parser.parse_args()
    
    def writeOnDatabase(self, value, status, filename, desc):
        date = time.strftime("%d/%m/%y")
        with open(filename, 'r') as file:
            data_temp = json.loads(file.read())
        
        stat = 0
        for i in data_temp.keys():
            if i == date:
                stat = 1
                print("Hari ini sudah ditulis")
                print(data_temp[i].keys())
                for j in data_temp[i].keys():
                    if j == status:
                        stat = 3
                        data_temp[i][status].update({desc:value})
                    else:
                        if stat == 3:
                            stat = 4
                            pass
                        else:
                            stat = 2
                        
            else:
                pass
        if stat == 2 :
            print('stat2')
            data_temp[date].update({status:{}})
            data_temp[date][status].update({desc:value})
        if stat == 0:
            print('stat3')
            data_temp.update({date:{}})
            data_temp[date].update({status:{}})
            data_temp[date][status].update({desc:value})
            
        with open(filename, 'w') as file:
            data_temp = json.dumps(data_temp)
            file.write(rf"{str(data_temp)}")
            
                
        print(data_temp)
        print(type(data_temp))
            
    
    
    def printResult(self):
        file_name = self.args.file
        desc_name = self.args.description
        if self.args.income != None:
            self.writeOnDatabase(value=self.args.income, status='income', filename=file_name, desc=desc_name)
            print("you write income")
        if self.args.outcome != None:
            self.writeOnDatabase(value=self.args.outcome, status='outcome', filename=file_name, desc=desc_name)
            print("you write outcome")
        
            
    

if __name__ == '__main__':
    mainapp = Program()
    mainapp.printResult()

