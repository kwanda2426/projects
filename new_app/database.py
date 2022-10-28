# import sqlite3
# 
# conn = sqlite3.connect('data1.db', check_same_thread=False)
# c = conn.cursor()
# 
# 
# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT, task_status TEXT, task_due_date DATE)')
# 
# 
# def add_data(task, task_status, task_due_date):
#     c.execute('INSERT INTO taskstable (task, task_status, task_due_date) VALUES (?,?,?)', (task, task_status, task_due_date))
#     conn.commit()
# 
# 
# def view_all_data():
#     c.execute('SELECT * FROM taskstable')
#     data = c.fetchall()
#     return data


import sqlite3
conn = sqlite3.connect('data9.db',check_same_thread=False)
conn2 = sqlite3.connect('data18.db',check_same_thread=False)

c = conn.cursor()
c2 = conn2.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE, mtrd_corelok TEXT, brd_corelok TEXT, voids_corelok TEXT)')


def add_data(task,task_status,task_due_date, mtrd_corelok, brd_corelok, voids_corelok):
	c.execute('INSERT INTO taskstable(task,task_status,task_due_date,mtrd_corelok,brd_corelok,voids_corelok) VALUES (?,?,?,?,?,?)',(task,task_status,task_due_date,mtrd_corelok, brd_corelok, voids_corelok))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM taskstable')
	data = c.fetchall()
	return data

def get_task(task):
	c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
	data = c.fetchall()
	return data

def get_task_by_status(task_status):
	c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
	data = c.fetchall()


def edit_task_data(new_task, new_task_status, new_task_due_date, new_mtrd_corelok,new_brd_corelok, new_voids_corelok\
                               , task, task_status, task_due_date, mtrd_corelok, brd_corelok, voids_corelok):
	c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=?,mtrd_corelok=?,brd_corelok=?,voids_corelok=? WHERE task=? and\
	 task_status =? and task_due_date =? and mtrd_corelok =? and brd_corelok =? and voids_corelok =?"\
	,(new_task, new_task_status, new_task_due_date, new_mtrd_corelok,new_brd_corelok, new_voids_corelok\
                               , task, task_status, task_due_date, mtrd_corelok, brd_corelok, voids_corelok))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task):
	c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
	conn.commit()





#########################################################################################################

def create_table_bn():
	c2.execute('CREATE TABLE IF NOT EXISTS taskstable(sample_id TEXT,date DATE,specification TEXT,penetration TEXT, softpoint TEXT, \
	vascosity_at_60 TEXT,vascosity_at_135 TEXT, after_rtfof_mass TEXT, after_rtfof_point TEXT, after_rtfof_vascosity TEXT)')







def add_data_bn(sample_id, date, specification, penetration, softpoint, vascosity_at_60,vascosity_at_135, after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity):

	c2.execute('INSERT INTO taskstable(sample_id, date, specification, penetration, softpoint, vascosity_at_60,vascosity_at_135, after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity) VALUES (?,?,?,?,?,?,?,?,?,?)',\
			  ( sample_id, date, specification, penetration, softpoint, vascosity_at_60,vascosity_at_135, after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity))
	conn2.commit()








def view_all_data_bn():
	c2.execute('SELECT * FROM taskstable')
	data = c2.fetchall()
	return data

def view_all_task_names_bn():
	c2.execute('SELECT DISTINCT sample_id FROM taskstable')
	data = c2.fetchall()
	return data

def get_task_bn(sample_id):
	c2.execute('SELECT * FROM taskstable WHERE sample_id="{}"'.format(sample_id))
	data = c2.fetchall()
	return data

def get_task_by_status_bn(specification):
	c2.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(specification))
	data = c2.fetchall()


def edit_task_data_bn(new_sample_id, new_date, new_specification, new_penetration, new_softpoint, new_vascosity_at_60,new_vascosity_at_135,new_after_rtfof_mass, new_after_rtfof_point, new_after_rtfof_vascosity\
                               ,sample_id, date, specification, penetration, softpoint, vascosity_at_60, vascosity_at_135,after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity):
	c2.execute("UPDATE taskstable SET sample_id =?,date=?, specification=?,penetration=?,softpoint=?,vascosity_at_60=?\
	,vascosity_at_135=?, after_rtfof_mass=?, after_rtfof_point=?, after_rtfof_vascosity=? WHERE sample_id=? and date=? and\
	 specification =? and penetration =? and softpoint =? and vascosity_at_60 =? and vascosity_at_135 =? and after_rtfof_mass=? and after_rtfof_point=? and after_rtfof_vascosity=? "\
	,(new_sample_id, new_date, new_specification, new_penetration, new_softpoint, new_vascosity_at_60,new_vascosity_at_135,new_after_rtfof_mass, new_after_rtfof_point, new_after_rtfof_vascosity\
                               ,sample_id, date, specification, penetration, softpoint, vascosity_at_60, vascosity_at_135,after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity))
	conn2.commit()
	data = c2.fetchall()
	return data

def delete_data_bn(sample_id):
	c2.execute('DELETE FROM taskstable WHERE sample_id="{}"'.format(sample_id))
	conn2.commit()
























