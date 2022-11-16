var hocSinh = [
  { ten: "huy", khoi: "A", diem: { toan: 7, van: 5, anh: 5 } },
  { ten: "lam", khoi: "B", diem: { toan: 7, van: 7, anh: 5 } },
  { ten: "tung", khoi: "C", diem: { toan: 7, van: 4, anh: 7 } }
];

var khoiThi = [
  { khoi: "A", heSo: { toan: 2, van: 1, anh: 1 }, diemSan: 25 },
  { khoi: "B", heSo: { toan: 1, van: 1, anh: 2 }, diemSan: 24 },
  { khoi: "C", heSo: { toan: 1, van: 2, anh: 1 }, diemSan: 20 }
];

/*
  1. hãy tính điểm thi của từng học sinh biết tổng điểm = điểm thi * hệ số
  2. hệ số sẽ thay đổi theo khối thi và môn thi
  3. hoc sinh thi đỗ nếu điểm thi >= điểm sàn của khối tương ứng
  4. hãy cho biết ai thi đỗ, ai thi trượt
-----
Need: Ten, Diem, va tu khoiThi lay he so tuong ung voi Hoc Sinh
*/

const ketQua = hocSinh.map((hs) => {
	let khoi = khoiThi.find((k) => k.khoi === hs.khoi)
	let diem = 0
	for (let mon in khoi.heSo){
		diem += hs.diem[mon] * khoi.heSo[mon]
	}
	return {
		"Student": hs.ten,
		"Class Subject": khoi,
		"Score": diem,
		"Floor-score": khoi.diemSan,
		"Result": diem >= khoi.diemSan ? "Pass": "Fail"
	}})

console.table(ketQua)


