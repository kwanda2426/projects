import streamlit as st
import pandas as pd
from database import *
import streamlit.components.v1 as stc
import time
timestr = time.strftime("%Y%m%d-%H%MS")
# Data Viz Pkgs
import plotly.express as px
import base64

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;"> Pavement Materials App</h1>
    <p style="color:white;text-align:center;">Built with Streamlit</p>
    </div>
    """

def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "new_text_file_{}_.csv".format(timestr)
    st.markdown("#### Download File ####")
    href = f'< href = "data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    # st.markdown(href, unsafe_allow_html=True)
    return href
    









def main():
    stc.html(HTML_BANNER)

    text = """
        ## Note: ##
        ---------------------
        **This is a dashboard to show an interactive report in an app.**\n

        ---------------------
        """
    st.sidebar.markdown(text)

    # Checkbox
    st.sidebar.subheader("Summary")

    st.sidebar.checkbox("Description of the data")



    # Asphalt = ["Create_Asphalt", "Read_Asphalt", "Update_Asphalt", "Delete_Asphalt",\
    #            "About_Asphalt", "Create_Binder", "Read_Binder", "Update_Binder", "Delete_Binder", "About_Binder"]

    Asphalt = ["Create_Asphalt", "Read_Asphalt", "Update_Asphalt", "Delete_Asphalt", "About_Asphalt"]
    # Binder = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Asphalt:", Asphalt)
    # choice_Binder = st.sidebar.selectbox("Binder", Binder)
    create_table()
    create_table_bn()

    if choice == "Create_Asphalt":
        st.subheader("Asphalt Data")
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_input("Sample ID")
            task_status = st.selectbox("MTRD_type", ["Corelok", "TMH1"])
            task_due_date = st.date_input("Date recorded")

        with col2:
            mtrd_corelok = st.number_input("MTRD")
            brd_corelok = st.number_input("BRD")
            voids_corelok = st.number_input("Voids (%)")

        if st.button("Store Asphalt Data", key='1'):
            add_data(task, task_status, task_due_date, mtrd_corelok, brd_corelok, voids_corelok)
            st.success("Sample {} added to database".format(task))


    elif choice == "Read_Asphalt":
        # st.subheader("View Items")
        with st.expander("View All Asphalt Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Sample ID", "MTRD_type", "Date recorded","mtrd","brd", "void"])

            clean_df_Corelok = clean_df[clean_df['MTRD_type']=='Corelok']
            clean_df_TMH1 = clean_df[clean_df['MTRD_type'] == 'TMH1']

            st.dataframe(clean_df)
            # csv_downloader(clean_df)
            
        # if st.button("download"):
            # csv_downloader(clean_df)

        with st.expander("mtrd_Corelok vs void_Corelok"):
            # task_df = clean_df['Status'].value_counts().to_frame()
            # st.dataframe(task_df)
            # task_df = task_df.reset_index()
            # st.dataframe(task_df)
            # p1 = px.pie(task_df, names='index', values='Status')
            # st.plotly_chart(p1, use_container_width=True)

            fig = px.line(clean_df_Corelok, x='mtrd', y="void")
            st.plotly_chart(fig, use_container_width=True)

        with st.expander("mtrd_TMH1 vs void_TMH1"):
            fig1 = px.line(clean_df_TMH1, x='mtrd', y="void")
            st.plotly_chart(fig1, use_container_width=True)

    elif choice == "Update_Asphalt":
        st.subheader("Edit Asphalt Data")
        with st.expander("Current Asphalt Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Sample ID", "MTRD_type", "Date recorded","mtrd","brd", "void"])
            st.dataframe(clean_df)

        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Search by sample ID", list_of_tasks)
        task_result = get_task(selected_task)
        # st.write(task_result)

        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_due_date = task_result[0][2]
            mtrd_corelok = task_result[0][3]
            brd_corelok = task_result[0][4]
            voids_corelok = task_result[0][5]


            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_input("Sample ID")
                new_task_status = st.selectbox("MTRD_type", ["Corelok", "TMH1"])
                new_task_due_date = st.date_input("Date recorded")
            with col2:
                new_mtrd_corelok = st.number_input("MTRD")
                new_brd_corelok = st.number_input(" BRD")
                new_voids_corelok = st.number_input("Voids (%)")

            if st.button("Update Asphalt Data"):
                edit_task_data(new_task, new_task_status, new_task_due_date, new_mtrd_corelok,new_brd_corelok, new_voids_corelok\
                               , task, task_status, task_due_date, mtrd_corelok, brd_corelok, voids_corelok)
                st.success("Data Updated from {} to {}".format(task, new_task))

            with st.expander("View Updated Asphalt Data"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result, columns=["Sample ID", "MTRD_type", "Date recorded","mtrd","brd", "void"])
                st.dataframe(clean_df)


    elif choice == "Delete_Asphalt":
        st.subheader("Delete Asphalt Data")
        with st.expander("View Asphalt Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Sample ID", "MTRD_type", "Date recorded","mtrd","brd", "void"])
            st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Select Task", unique_list)
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

        with st.expander("Updated Asphalt Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Sample ID", "MTRD_type", "Date recorded","mtrd","brd", "void"])
            st.dataframe(clean_df)

    # else:
    #     st.subheader("About App")
    #     st.info("Built with Streamlit")
        # st.info("Jesus Saves @JCharisTech")
        # st.text("Jesse E.Agbe(JCharis)")
    ##############################################################################################


####################################################################################################


    Binder = ("Create_Binder", "Read_Binder", "Update_Binder", "Delete_Binder", "About_Binder")
    # choice1 = st.sidebar.selectbox("Binder:", Binder)
    choice1 = st.sidebar.radio("Binder:", Binder)

    if choice1 == "Create_Binder":
        st.subheader("Binder Data")
        col1, col2 = st.columns(2)

        with col1:
            sample_id = st.text_input("Sample ID_")
            date = st.date_input("Date recorded")
            specification = st.number_input('Specification')
            penetration = st.number_input("Penetration (mm x 10 ^-1)")
            softpoint = st.number_input("Soft Point (C)")
        with col2:
            vascosity_at_60 = st.number_input("Vascosity at 60C ")
            vascosity_at_135 = st.number_input("Vascosity at 135C ")
            after_rtfof_mass = st.number_input("Mass Change ")
            after_rtfof_point = st.number_input("Soft Point")
            after_rtfof_vascosity = st.number_input("Vascosity")




        if st.button("Store Binder data", key="2"):
            add_data_bn(sample_id, date, specification, penetration, softpoint, vascosity_at_60,\
                       vascosity_at_135,after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity)
            st.success("Sample {} added to database".format(sample_id))


    elif choice1 == "Read_Binder":
        # st.subheader("View Items")
        with st.expander("View All Binder Data"):
            result = view_all_data_bn()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["sample_id", "date", "specification","penetration","softpoint", "vascosity_at_60"\
                                                     , "vascosity_at_135", "after_rtfof_mass",'after_rtfof_point', 'after_rtfof_vascosity'])
            st.dataframe(clean_df)

        with st.expander("specification vs specification"):
            # task_df = clean_df['penetration'].value_counts().to_frame()
            # st.dataframe(task_df)
            # task_df = task_df.reset_index()
            # st.dataframe(task_df)
            # p1 = px.pie(task_df, names='index', values='penetration')
            # st.plotly_chart(p1, use_container_width=True)

            fig = px.line(clean_df, x='penetration', y="specification")
            # fig.show()
            st.plotly_chart(fig, use_container_width=True)

    elif choice1 == "Update_Binder":
        st.subheader("Edit Binder Data")
        with st.expander("Current Data"):
            result = view_all_data_bn()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["sample_id", "date", "specification","penetration","softpoint", "vascosity_at_60"\
                                                     , "vascosity_at_135", "after_rtfof_mass",'after_rtfof_point', 'after_rtfof_vascosity'])
            st.dataframe(clean_df)

        list_of_tasks = [i[0] for i in view_all_task_names_bn()]
        selected_task = st.selectbox("Search by sample ID", list_of_tasks)
        task_result = get_task_bn(selected_task)
        # st.write(task_result)

        if task_result:
            sample_id = task_result[0][0]
            date = task_result[0][1]
            specification = task_result[0][2]
            penetration = task_result[0][3]
            softpoint = task_result[0][4]
            vascosity_at_60 = task_result[0][5]
            vascosity_at_135 = task_result[0][6]
            after_rtfof_mass = task_result[0][7]
            after_rtfof_point = task_result[0][8]
            after_rtfof_vascosity = task_result[0][9]

            col1, col2 = st.columns(2)

            with col1:

                new_sample_id = st.text_input("Sample ID_")
                new_date = st.date_input("Date recorded")
                new_specification = st.number_input('specification')
                new_penetration = st.number_input("Penetration (mm x 10 ^-1)")
                new_softpoint = st.number_input("Soft Point (C)")

            with col2:
                new_vascosity_at_60 = st.number_input("vascosity at 60C ")
                new_vascosity_at_135 = st.number_input("vascosity at 135C ")
                new_after_rtfof_mass = st.number_input("Mass Change ")
                new_after_rtfof_point = st.number_input("Soft Point")
                new_after_rtfof_vascosity = st.number_input("vascosity")



            if st.button("Update Binder Data"):
                edit_task_data_bn(new_sample_id, new_date, new_specification, new_penetration, new_softpoint, new_vascosity_at_60,new_vascosity_at_135,new_after_rtfof_mass, new_after_rtfof_point, new_after_rtfof_vascosity\
                               ,sample_id, date, specification, penetration, softpoint, vascosity_at_60,vascosity_at_135,after_rtfof_mass, after_rtfof_point, after_rtfof_vascosity)
                st.success("Data Updated from {} to {}".format(sample_id, new_sample_id))

            with st.expander("View Updated Binder Data"):
                result = view_all_data_bn()
                # st.write(result)
                clean_df = pd.DataFrame(result, columns=["sample_id", "date", "specification","penetration","softpoint", "vascosity_at_60"\
                                                     , "vascosity_at_135", "after_rtfof_mass",'after_rtfof_point', 'after_rtfof_vascosity'])
                st.dataframe(clean_df)


    elif choice1 == "Delete_Binder":
        st.subheader("Delete Binder Data")
        with st.expander("View Binder Data"):
            result = view_all_data_bn()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["sample_id", "date", "specification","penetration","softpoint", "vascosity_at_60"\
                                                     , "vascosity_at_135", "after_rtfof_mass",'after_rtfof_point', 'after_rtfof_vascosity'])
            st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names_bn()]
        delete_by_task_name = st.selectbox("Search by sample ID", unique_list)
        if st.button("Delete"):
            delete_data_bn(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

        with st.expander("Binder Data Updated"):
            result = view_all_data_bn()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["sample_id", "date", "specification","penetration","softpoint", "vascosity_at_60"\
                                                     , "vascosity_at_135", "after_rtfof_mass",'after_rtfof_point', 'after_rtfof_vascosity'])
            st.dataframe(clean_df)

    else:
        st.subheader("About App")
        st.info("Built with Streamlit")
        # st.info("Jesus Saves @JCharisTech")
        # st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
    main()