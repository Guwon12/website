
Django Movie Streaming Website
Đây là dự án website xem phim được xây dựng bằng Python và Django nhằm mục đích học tập và phát triển kỹ năng lập trình web. Nếu bạn thấy dự án hữu ích, hãy ⭐️ Star để ủng hộ nhé! 


CHỨC NĂNG CHÍNH
Người quản trị (Admin) có thể:
•	Quản lý danh sách phim: Thêm, sửa, xóa phim.
•	Quản lý người dùng 
•	Xem thống kê tổng quan về phim và đánh gía
Người dùng (User) có thể:
•	Tìm kiếm phim theo tên.
•	Xem danh sách phim, chi tiết phim và video.
•	Quản lý tài khoản cá nhân.
________________________________________
CÁCH CÀI ĐẶT VÀ CHẠY DỰ ÁN
Yêu cầu trước khi cài đặt
•	Cài Git: https://git-scm.com/
•	Cài Python (phiên bản mới nhất): https://www.python.org/downloads/
•	Cài pip: https://pip.pypa.io/en/stable/installation/
Các bước cài đặt
1.	Tạo thư mục lưu dự án.
2.	Tạo và kích hoạt môi trường ảo:
o	Windows:
o	python -m venv venv
o	venv\Scripts\activate
o	Mac/Linux:
o	python3 -m venv venv
o	source venv/bin/activate
3.	Clone source code:
4.	git clone https://github.com/Guwon12/website
5.	Cài đặt các gói phụ thuộc:
	pip install -r requirements.txt
7.	Chỉnh sửa settings.py, thêm dòng sau để cho phép tất cả host (chỉ dùng khi phát triển):
	ALLOWED_HOSTS = ['*']
9.	Khởi chạy server:
o	Windows:
o	python manage.py runserver
o	Mac/Linux:
o	python3 manage.py runserver
10.	Tạo tài khoản quản trị:
	python manage.py createsuperuser
Nhập email, username, mật khẩu theo yêu cầu.
________________________________________

