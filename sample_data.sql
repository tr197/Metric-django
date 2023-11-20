INSERT INTO public.shop_platform (name,image) VALUES
	 ('Shopee','media/shop/flatform/shopee.png'),
	 ('Tiki','media/shop/flatform/tiki.png'),
	 ('Lazada','media/shop/flatform/lazada.png');

INSERT INTO public.category_base (id,name,slug,create_date,update_date) VALUES
	 ('8c0f1444-bef3-41ba-b714-fbefebe1aee8','Laptop','laptop','2023-11-19','2023-11-19'),
	 ('8ee01350-e955-49f3-9740-92013a99247a','Phụ kiện','phu-kien','2023-11-19','2023-11-19'),
	 ('6cf426d7-2038-49b4-a102-c71fdcb26ed8','Màn hình','man-hinh','2023-11-19','2023-11-19'),
	 ('158242dc-07af-40b3-bb95-c077a87758d8','Linh kiện build PC','linh-kien-build-pc','2023-11-19','2023-11-19'),
	 ('f5c597ff-0696-4dfc-bb37-03b53348014a','Laptop doanh nhân','laptop-doanh-nhan','2023-11-19','2023-11-19'),
	 ('8c4efd5e-f4b2-416b-8a22-6224ede0dd71','Laptop văn phòng','laptop-van-phong','2023-11-19','2023-11-19'),
	 ('24786e11-dee8-49ce-b023-a5fa69f7c8ee','Laptop Gamming','laptop-gamming','2023-11-19','2023-11-19'),
	 ('f52d0049-f26c-4dae-8aad-15b5ab235db0','Bàn phím','ban-phim','2023-11-20','2023-11-20');
	
INSERT INTO public.category (categorybase_ptr_id) VALUES
	 ('8c0f1444-bef3-41ba-b714-fbefebe1aee8'),
	 ('158242dc-07af-40b3-bb95-c077a87758d8'),
	 ('8ee01350-e955-49f3-9740-92013a99247a'),
	 ('6cf426d7-2038-49b4-a102-c71fdcb26ed8'),
	 ('f52d0049-f26c-4dae-8aad-15b5ab235db0');

INSERT INTO public.category_sub (categorybase_ptr_id,parent_id) VALUES
	 ('f5c597ff-0696-4dfc-bb37-03b53348014a','8c0f1444-bef3-41ba-b714-fbefebe1aee8'),
	 ('8c4efd5e-f4b2-416b-8a22-6224ede0dd71','8c0f1444-bef3-41ba-b714-fbefebe1aee8'),
	 ('24786e11-dee8-49ce-b023-a5fa69f7c8ee','8c0f1444-bef3-41ba-b714-fbefebe1aee8');
	
	
INSERT INTO public.product (id,name,slug,create_date,update_date,description,image,price,category_id) VALUES
	 ('ce00e83f-70bc-4129-abb0-d34bae50cf58','Dell XPS 5531','dell-xps-5531','2023-11-19','2023-11-19','The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.','media/product/main/dell_xps_13_9315_trungtran_vn.png',999999999,'f5c597ff-0696-4dfc-bb37-03b53348014a'),
	 ('d26c735f-93be-474a-bc19-31872bf690b2','HP Victus','hp-victus','2023-11-19','2023-11-19','(venv) trinh@ubuntuPC:~/PRJS/Metric/DJ4/code$ python manage.py migrate
Operations to perform:
  Apply all migrations: account, admin, auth, contenttypes, product, sessions','media/product/main/hpvitus.png',12223434,'24786e11-dee8-49ce-b023-a5fa69f7c8ee'),
	 ('3c113bed-898f-4f31-91d6-c00b13205e9d','Asus Vivobook','asus-vivobook','2023-11-19','2023-11-19','[19/Nov/2023 05:08:16] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 304 0
[19/Nov/2023 05:08:16] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[19/Nov/2023 05:08:16] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0','media/product/main/x1504va-1_638264189418692393.webp',999999999,'8c0f1444-bef3-41ba-b714-fbefebe1aee8'),
	 ('e957a09a-14db-4e56-849b-972682015e3b','Thinkpad T490','thinkpad-t490','2023-11-19','2023-11-20','Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying account.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK','media/product/main/thinkpad-t490.webp',999999999,'f5c597ff-0696-4dfc-bb37-03b53348014a');


INSERT INTO public.product_comment (username,"content",create_date,update_date,product_id) VALUES
	 ('trinh','sản phầm đẹp abc abc','2023-11-20','2023-11-20','e957a09a-14db-4e56-849b-972682015e3b'),
	 ('ronaldo','sản phẩm hơi đẹp xyz xyz','2023-11-20','2023-11-20','e957a09a-14db-4e56-849b-972682015e3b');

INSERT INTO public.product_image (image,product_id) VALUES
	 ('media/product/other/5603_lenovo_thinkpad_t490_6.jpg','e957a09a-14db-4e56-849b-972682015e3b'),
	 ('media/product/other/thinkpad-t490.webp','e957a09a-14db-4e56-849b-972682015e3b'),
	 ('media/product/other/assss.jpg','3c113bed-898f-4f31-91d6-c00b13205e9d');

INSERT INTO public.product_option (name,price,product_id,platform_id,sale_count,link) VALUES
	 ('Applying product 0005 remove productoptions_',25000001,'e957a09a-14db-4e56-849b-972682015e3b',2,4,'/'),
	 ('Apply all migrations: account, admin, auth',25000000,'e957a09a-14db-4e56-849b-972682015e3b',1,3,'https://shopee.vn/Laptop-Lenovo-ThinkPad-T490-I7-10510U-RAM-16GB-SSD-512GB-14-FHD.-i.164318637.10759439874');

