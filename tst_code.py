import nacl.pwhash
from config import get_user_detail
import hashlib

pwd = "my pas"

# user, pwd = get_user_detail()
# Password used to hash itself
# orig_password = bytes(pwd, encoding="ascii")
# orig_password = b'my password'

# Hashing the password
# hashed_data = nacl.pwhash.str(orig_password)
# print(hashed_data)

# decode_data = hashed_data.decode("utf-8")
# print(decode_data)
# print(type(decode_data))

# The result will be True on password match.
# res = nacl.pwhash.verify(hashed_data, orig_password)
# print(res)

# On mismatch an exception will be raised
# wrong_password = b'my password'
# res2 = nacl.pwhash.verify(hashed_data, wrong_password)


"""
with "CTEdak" as (
	select  g."KodeKebun", f."KodeDivisi", date_part('year', a.TanggalAbsen) "Tahun", date_part(month(a.TanggalAbsen) Bulan, a.TanggalAbsen,
		a.ID_Ms_KaryawanKebun, d.Keterangan NamaKelompok, e.Nama Jabatan
	from Tr_DaftarAbsensiKaryawan a
	join Ms_Absensi b on a.ID_Ms_Absensi = b.ID_Ms_Absensi
	join (
		select YEAR(b.TanggalBukaPeriode) Tahun, month(b.TanggalBukaPeriode) Bulan, a.ID_Ms_Jabatan, a.ID_Ms_Kelompok, a.ID_Ms_KaryawanKebun
		from Log_Ms_KaryawanKebunPeriodik a
		join Ms_PengaturanPeriode b on a.ID_Ms_PengaturanPeriode = b.ID_Ms_PengaturanPeriode
		where tahun = 2023 ) c on a.ID_Ms_KaryawanKebun = c.ID_Ms_KaryawanKebun and year(a.TanggalAbsen) = c.Tahun and month(a.TanggalAbsen) = c.Bulan
	join Ms_Kelompok d on c.ID_Ms_Kelompok = d.ID_Ms_Kelompok
	join Ms_Jabatan e on c.ID_Ms_Jabatan = e.ID_Ms_Jabatan
	join Ms_DivisiKebun f on d.ID_Ms_DivisiKebun = f.ID_Ms_DivisiKebun
	join Ms_Kebun g on f.ID_Ms_Kebun = g.ID_Ms_Kebun
	where year(TanggalAbsen) = 2023 and month(a.TanggalAbsen) = 8
	and a.ModifyStatus <> 'D'
and b.KodeAbsensi in ('TL','KR','KM','KL','K','GT','A')
),

CTEdakp as (
	select g.KodeKebun, f.KodeDivisi,a.TanggalAbsen, a.ID_Ms_KaryawanKebun, d.Keterangan NamaKelompok
	from Tr_DaftarAbsensiKaryawan a
	join Ms_Absensi b on a.ID_Ms_Absensi = b.ID_Ms_Absensi
	join Tr_PindahKelompok c on a.ID_Tr_DaftarAbsensiKaryawan = c.ID_Tr_DaftarAbsensiKaryawan and c.ModifyStatus <> 'D'
	join Ms_Kelompok d on c.ID_Ms_Kelompok = d.ID_Ms_Kelompok
	join Ms_DivisiKebun f on d.ID_Ms_DivisiKebun = f.ID_Ms_DivisiKebun
	join Ms_Kebun g on f.ID_Ms_Kebun = g.ID_Ms_Kebun
	where year(TanggalAbsen) = 2023 and month(a.TanggalAbsen) = 8
	and a.ModifyStatus <> 'D'
and b.KodeAbsensi in ('TL','KR','KM','KL','K','GT','A')
),

CTEjoin as (
select a.TanggalAbsen, a.ID_Ms_KaryawanKebun, a.Jabatan,
	case when b.NamaKelompok is not null then b.KodeKebun else a.KodeKebun end KodeKebun,
	case when b.NamaKelompok is not null then b.KodeDivisi else a.KodeDivisi end KodeDivisi,
	case when b.NamaKelompok is not null then b.NamaKelompok else a.NamaKelompok end NamaKelompok
from CTEdak a
left join CTEdakp b on a.TanggalAbsen = b.TanggalAbsen and a.ID_Ms_KaryawanKebun = b.ID_Ms_KaryawanKebun
)

--select * from CTEjoin

select KodeKebun, KodeDivisi, TanggalAbsen, a.NamaKelompok, a.Jabatan, count(ID_Ms_KaryawanKebun) TK
from CTEjoin a
--join Ms_Jabatan b on a.ID_Ms_Jabatan = b.ID_Ms_Jabatan
--join Ms_Kelompok c on a.ID_Ms_Kelompok = c.ID_Ms_Kelompok
group by KodeKebun, KodeDivisi, TanggalAbsen, a.NamaKelompok, a.Jabatan
"""
