import sqlite3


DbName = 'Uangku.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()

class item :
    def __init__(self,keterangan,nominalSatuan,jumlah,totalNominal,tanggal):
        self.__keterangan = keterangan
        self.__nominalSatuan = nominalSatuan
        self.__jumlah = jumlah
        self.__totalNominal = totalNominal
        self.__tanggal = tanggal

    def get_keterangan(self):
        return self.__keterangan

    def get_nominalSatuan(self):
        return self.__nominalSatuan

    def get_jumlah(self):
        return self.__jumlah

    def get_totalNominal(self):
        return self.__totalNominal

    def get_tanggal(self):
        return self.__tanggal

class pendapatan(item):
    def __init__(self,namaPendapatan,tanggal,nominalSatuan,jumlah,totalNominal,keterangan):
        super().__init__(keterangan,nominalSatuan,jumlah,totalNominal,tanggal)
        self.__namaPendapatan = namaPendapatan

    def get_namaPendapatan(self):
        return self.__namaPendapatan

class pengeluaran(item) :
    def __init__(self,namaPengeluaran,tanggal, nominalSatuan, jumlah, totalNominal, keterangan):
        super().__init__(keterangan,nominalSatuan,jumlah,totalNominal,tanggal)
        self.__namaPenengeluaran=namaPengeluaran

    def get_namaPengeluaran(self):
        return self.__namaPenengeluaran



conn.execute(
    "CREATE TABLE IF NOT EXISTS Pendapatan (id_pendapatan INTEGER PRIMARY KEY AUTOINCREMENT,tanggal date,namaPendapatan text,nominalSatuan integer,jumlah integer ,totalNominal integer,keterangan text)"
)
conn.execute(
    "CREATE TABLE IF NOT EXISTS pengeluaran (id_pengeluaran INTEGER PRIMARY KEY AUTOINCREMENT,tanggal date,namaPengeluaran text,nominalSatuan integer,jumlah integer ,totalNominal integer,keterangan text)"
)

def insertPendapatan():
    namaPendapatan = input("masukkan nama Pendapatan:")
    tanggal = input("masukkan tanggal (YYYY-MM-DD) :")
    nominalSatuan = int(input("nominal satuan :"))
    jumlah = int(input("jumlah :"))
    totalNominal=(nominalSatuan*jumlah)
    keterangan = input("keterangan :")

    dapat=pendapatan(namaPendapatan,tanggal, nominalSatuan, jumlah, totalNominal, keterangan)
    conn.execute("INSERT INTO pendapatan (tanggal,namaPendapatan, nominalSatuan, jumlah, totalNominal, keterangan) values (?,?,?,?,?,?)",(dapat.get_tanggal(),dapat.get_namaPendapatan(),dapat.get_nominalSatuan(), dapat.get_jumlah(), dapat.get_totalNominal(), dapat.get_keterangan()))

def insertPengeluaran():
    namaPengeluaran = input("masukkan nama Pengeluaran:")
    tanggal = input("masukkan tanggal (YYYY-MM-DD) :")
    nominalSatuan = int(input("nominal satuan :"))
    jumlah = int(input("jumlah :"))
    totalNominal=(nominalSatuan*jumlah)
    keterangan = input("keterangan :")

    dapat=pengeluaran(namaPengeluaran,tanggal, nominalSatuan, jumlah, totalNominal, keterangan)
    conn.execute("INSERT INTO Pengeluaran (tanggal,namaPengeluaran, nominalSatuan, jumlah, totalNominal, keterangan) values (?,?,?,?,?,?)",(dapat.get_tanggal(),dapat.get_namaPengeluaran(),dapat.get_nominalSatuan(), dapat.get_jumlah(), dapat.get_totalNominal(), dapat.get_keterangan()))

def readTabelPendapatan():
    cursor=conn.cursor().execute('SELECT * FROM Pendapatan')
    for row in cursor:
          print(f"""
          id_pendapatan : {row[0]}
          tanggal: {row[1]}
          nama pendapatan: {row[2]}
          nominal satuan: {row[3]}
          jumlah: {row[4]}
          total nominal: {row[5]}
          Keterangan: {row[6]}""")

def readTabelPengeluaran():
    cursor=conn.cursor().execute('SELECT * FROM Pengeluaran')
    for row in cursor:
          print(f"""
          id_pengeluaran : {row[0]}
          tanggal: {row[1]}
          nama pengeluaran: {row[2]}
          nominal satuan: {row[3]}
          jumlah: {row[4]}
          total nominal: {row[5]}
          Keterangan: {row[6]}""")

def UpdatePendapatan(keterangan , totalNominal,jumlah,nominalSatuan,namaPendapatan,tanggal,id_pendapatan):
    conn.cursor().execute("""update pendapatan set keterangan = ?,totalNominal = ?,jumlah = ?,nominalSatuan = ?,namaPendapatan = ?,tanggal = ? where id_pendapatan = ?""", (keterangan,totalNominal,jumlah,nominalSatuan,namaPendapatan,tanggal,id_pendapatan))
    conn.commit()

def UpdatePengeluaran(keterangan , totalNominal,jumlah,nominalSatuan,namaPengeluaran,tanggal,id_pengeluaran):
    conn.cursor().execute("""update Pengeluaran set keterangan = ?,totalNominal = ?,jumlah = ?,nominalSatuan = ?,namaPengeluaran = ?,tanggal = ? where id_pengeluaran = ?""", (keterangan,totalNominal,jumlah,nominalSatuan,namaPengeluaran,tanggal,id_pengeluaran))
    conn.commit()

def DeletebyIdPengeluaran(id_pengeluaran):
    conn.execute('DELETE from pengeluaran WHERE id_pengeluaran = ?',(id_pengeluaran,))
    conn.commit()

def DeletebyIdPendapatan(id_pendapatan):
    conn.execute('DELETE from Pendapatan WHERE id_pendapatan = ?',(id_pendapatan,))
    conn.commit()


def dashboard():
    cursora = conn.cursor().execute('SELECT * FROM Pendapatan')
    x = 0
    for row in cursora:
        x = x + row[5]
    cursorb = conn.cursor().execute('SELECT * FROM Pengeluaran')
    y = 0
    for row in cursorb:
        y = y + row[5]
    print("total pendapatan : {} \n,total Pengeluaran : {} \n,sisa saldo: {} \n".format(x,y,x-y))
    a=input("""
    =============================================
                        MENU
    =============================================
    Silahkan pilih menu yang anda inginkan:
    [a] lihat data
    [b] Tabahkan data
    [c] Ubah Data 
    [d] Hapus data
    =============================================
    masukkan huruf yang diinginkan :
    """)
    if ( a=="a" ) :
        b= input("""
        =============================================
                       lihat data
        =============================================
        Silahkan lihat data yang anda inginkan:
        [a] seluruhnya
        [b] pendapatan
        [c] pengeluaran
        =============================================
        masukkan huruf yang diinginkan :
        """)
        if (b=="a") :
           readTabelPendapatan()
           readTabelPengeluaran()
        elif(b=="b") :
            readTabelPendapatan()
        else :
            readTabelPengeluaran()
    elif(a=="b"):
        b= input("""
        =============================================
                       Tabahkan data
        =============================================
        Silahkan Tabahkan data yang anda inginkan:
        [a] Pendapatan
        [b] pengeluaran
        =============================================
        masukkan huruf yang diinginkan :
        """)
        if(b=="a") :
            insertPendapatan()
        else :
            insertPengeluaran()
    elif (a == "c"):
        b = input("""
            =============================================
                           Ubah Data 
            =============================================
            Silahkan Ubah Data  yang anda inginkan:
            [a] Pendapatan
            [b] pengeluaran
            =============================================
            masukkan huruf yang diinginkan :
            """)
        if (b == "a"):
            c=input("apakah sudah tau id_pendapatan yang di ubah \n [a]sudah [b] belum \n masukkan hurufnya :")
            if (c=="a") :
                readTabelPendapatan()
                id_pendapatan=int(input("silahkan input id_pengeluaran"))
                tanggal = input("silahkan input tanggal baru(DD-MM-YYYY)")
                namaPendapatan = input("silahkan input namaPengeluaran baru")
                nominalSatuan = int(input("silahkan input nominalSatuan baru"))
                jumlah = int(input("silahkan input jumlah baru"))
                totalNominal = nominalSatuan * jumlah
                keterangan = input("silahkan input keterangan baru")


                UpdatePendapatan(keterangan, totalNominal, jumlah, nominalSatuan, namaPendapatan, tanggal,id_pendapatan)

                readTabelPendapatan()
            else :
                id_pendapatan = int(input("silahkan input id_pengeluaran"))
                tanggal = input("silahkan input tanggal baru(DD-MM-YYYY)")
                namaPendapatan = input("silahkan input namaPengeluaran baru")
                nominalSatuan = int(input("silahkan input nominalSatuan baru"))
                jumlah = int(input("silahkan input jumlah baru"))
                totalNominal = nominalSatuan * jumlah
                keterangan = input("silahkan input keterangan baru")

                UpdatePendapatan(keterangan, totalNominal, jumlah, nominalSatuan, namaPendapatan, tanggal,
                                 id_pendapatan)

                readTabelPendapatan()
        else:
            c=input("apakah sudah tau id_pengeluaran yang di ubah \n [a]sudah [b] belum \n masukkan hurufnya :")
            if (c=="a"):
                readTabelPengeluaran()
                id_pengeluaran = int(input("silahkan input id_pengeluaran"))
                tanggal = input("silahkan input tanggal baru(DD-MM-YYYY)")
                namaPengeluaran = input("silahkan input namaPengeluaran baru")
                nominalSatuan = int(input("silahkan input nominalSatuan baru"))
                jumlah = int(input("silahkan input jumlah baru"))
                totalNominal = nominalSatuan * jumlah
                keterangan = input("silahkan input keterangan baru")

                UpdatePengeluaran(keterangan, totalNominal, jumlah, nominalSatuan, namaPengeluaran, tanggal, id_pengeluaran)

                readTabelPengeluaran()
            else :
                id_pengeluaran = int(input("silahkan input id_pengeluaran"))
                tanggal = input("silahkan input tanggal baru(DD-MM-YYYY)")
                namaPengeluaran = input("silahkan input namaPengeluaran baru")
                nominalSatuan = int(input("silahkan input nominalSatuan baru"))
                jumlah = int(input("silahkan input jumlah baru"))
                totalNominal = nominalSatuan * jumlah
                keterangan = input("silahkan input keterangan baru")

                UpdatePengeluaran(keterangan, totalNominal, jumlah, nominalSatuan, namaPengeluaran, tanggal,
                                  id_pengeluaran)

                readTabelPengeluaran()
    else:
        b = input("""
        =============================================
                        Ubah Data 
        =============================================
        Silahkan Ubah Data  yang anda inginkan:
        [a] Pendapatan
        [b] pengeluara
        =============================================
        masukkan huruf yang diinginkan :
        """)
        if(b=="a") :
            c = input("apakah sudah tau id_pendapatan yang di ubah \n [a]sudah [b] belum \n masukkan hurufnya :")
            if(c=="a") :
                id_pendapatan=int(input("masukkan id_pendapatan :"))
                DeletebyIdPendapatan(id_pendapatan)

                readTabelPendapatan()
            else:
                readTabelPendapatan()
                id_pendapatan = int(input("masukkan id_pendapatan :"))
                DeletebyIdPendapatan(id_pendapatan)

                readTabelPendapatan()
        else:
            c = input("apakah sudah tau id_pengeluaran yang di ubah \n [a]sudah [b] belum \n masukkan hurufnya :")
            if (c == "a"):
                id_pengeluaran = int(input("masukkan id_pengeluaran :"))
                DeletebyIdPengeluaran(id_pengeluaran)
                readTabelPengeluaran()
            else:
                readTabelPengeluaran()
                id_pengeluaran = int(input("masukkan id_pengeluaran :"))
                DeletebyIdPendapatan(id_pengeluaran)

                readTabelPengeluaran()
    conn.commit()
    dashboard()


dashboard()

conn.commit()