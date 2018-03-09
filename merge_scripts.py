# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :merge all the sql scripts
#
# Pre-requests: n/a
# History     :
# DATE        AUTHOR          DESCRIPTION
# ----------  ----------      ----------------------------------------------------
# 03/06/2018  - eliu2         - created
#
# @CopyRight  :
# -------------------------------------------------------------------------------

import os, re
import file_handler as fh
import constraint_handler as cons
import FK_handler as fk
import function_handler as func
import index_handler as idx
import PK_handler as pk
import sp_handler as sp
import table_handler as tb
import trigger_handler as tr
import UK_handler as uk
import view_handler as vw


def search_file_in_folder(file_name, folder_path):
    file_path = None
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        for f in files:
            if f == file_name:
                file_path = os.path.join(folder_path, f)
                break
    return file_path


def merge_scripts_in_order(script_list, parent_folder, w_file):
    for h_file in script_list:
        file_path = search_file_in_folder(h_file, parent_folder)
        if file_path is not None and os.path.isfile(file_path):
            context = fh.read_file(file_path)
            context = "\r\n" + context
            fh.write_file(w_file, context, 'utf-8', 'a')


def merge_views(script_list, folder, w_file):
    merge_scripts_in_order(script_list, folder, w_file)  # merged first
    files = os.listdir(folder)
    for file in files:
        if file in script_list:
            continue # this kind of file has been merged
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            context = fh.read_file(f)
            context = "\r\n" + context
            fh.write_file(w_file, context, 'utf-8', 'a')


def merge_special_scripts(script_list, w_file):
    for f in script_list:
        if os.path.isfile(f):
            context = fh.read_file(f)
            context = "\r\n" + context
            fh.write_file(w_file, context, 'utf-8', 'a')


def get_enums(path):
    enum_list =[]
    files = os.listdir(path)
    for f in files:
        pattern = re.compile(r'^dbo.Enum_')
        if pattern.search(f):
            enum_list.append(path + '\\' + f)
    return enum_list


root_dir = "E:\\Work-RAOutdoors\\CA\\AspiraFocusDB"


def merge_all_scripts():
    # absolute path
    trunk_dir = root_dir + '\\UniversalDatabasesCodes\\Databases'
    child_folders = ('Databases', 'Tables', 'PrimaryKeys', 'ForeignKeys', 'Indexes', 'Enums',
                     r"UserDefinedDataTypes", 'SpecialScripts', r'UserFunctions', 'Views',
                     'StoredProcedures', 'Triggers', 'Constraints',  r'UniqueKeys')
    script_name = 'DB_Deployment_v1.0.0.sql'

    view_list = ["dbo.adhoc_Phone.view.sql",
                 "dbo.adhoc_Address.view.sql" ,
                 "dbo.adhoc_Customer.view.sql",
                 "dbo.vw_AnnualIssuance_CustomerMailing.view.sql"
                 ]
    moved_files = [trunk_dir + '\\UserFunctions\\dbo.udf_GetCustomerName.function.sql',
                   trunk_dir + '\\Views\\dbo.vw_ControlledInventory_OutletStatusCount.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_ConfigValueComplete_Effective.view.sql',
                   trunk_dir + '\\Views\\dbo.adhoc_license.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CurrentCustomerVesselName.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerVesselAllOwnership.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerAddress.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_StockOnHand.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerVesselCurrentOwnership.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitRelatedCustomer.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LifetimeAnnualIssuanceCustomerSearch_Live.view.sql',
                   trunk_dir + '\\Views\\dbo.Diag_ItemFeeDist_CompleteTotals.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_ActiveAddress.view.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_GetCustomerIdentity.function.sql',

                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerBusiness.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_AnnualIssuance_CustomerPurchase.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_Item_LifetimeEnablingItem.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_AnnualIssuance_CustomerHasEnablingItem.view.sql',

                   trunk_dir + '\\UserFunctions\\dbo.udf_Search_LicenseReportAnswerGroup_ForDataExtracts.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_Renewal_Customers.function.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselOwnershipCurrent.view.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_Search_Renewal_Customers.function.sql',

                   trunk_dir + '\\UserFunctions\\dbo.udf_GetHighestPriorityDocumentTitleByDocumentID.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_Renewal_Items.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_Search_CustomerSimple.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_PreviouslyReportedCount.function.sql',

                   trunk_dir + '\\UserFunctions\\dbo.udf_RoundToTheNearest.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_GetGlobalDistribution.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_CatalogAllFees.function.sql',
                   trunk_dir + '\\Views\\dbo.vw_ItemSalesFee_All.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerVesselHomePortVesselPortCurrent.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_AnnualIssuance_PurchaseTotalByPackage.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_HuntDrawGroup.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_MasterHuntType_Complete.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_DrawConfig_Complete.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_HuntTypeLicenseYear_Complete.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_FulfillmentMostRecentDocumentFulfillmentAction.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_transactiondetail.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitTypeEx.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitEx.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitAnnualDesignationEx.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_LEPermitHerringPlatoonSpecial.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitHerringPlatoonDesignationInfo.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitTemporaryTransferEx.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_LEPermitHerringSquareView.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_LifetimeAnnualIssuanceSummary_LivePackageCustomerList.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerActiveAddressReturnPreferred.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_rpt_VesselCustomersOnly.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselOwnership.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselHomePortVesselPortCurrent.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_HerringAreaPlatoon.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_LEPermitAnnualDesignation.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_LEPermitLEPermitAnnualDesignationCurrent.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_LEPermitTemporaryTransfer.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_LEPermitType.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselDocumentationCurrent.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselCurrentOwnershipDocumentationHomePort.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_AnnualIssuance_JobResultSubTotals.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_AnnualIssuance_JobResultTotalByMailing.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_HuntApplicationParticipants.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselDocumentation.view.sql',

                   trunk_dir + '\\Views\\dbo.vw_LifetimeAnnualIssuanceCustomerSearch_PostIssuance.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerUnifiedNameAndIdentities.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_SLMSParticipantInfo.view.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_Search_SPFalconDispositionHistory.function.sql',

                   trunk_dir + '\\UserFunctions\\dbo.udf_Config_GetValueByKey_Effective.function.sql',
                   trunk_dir + '\\Views\\dbo.vw_SLMSLettersConfigurationValues.view.sql',

                   trunk_dir + '\\Views\\dbo.Diag_ItemFeeDist_FixedTotals.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerVesselHomePortVesselPort.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerOfficalDocument.view.sql',

                   trunk_dir + '\\UserFunctions\\dbo.udf_ConvertHeight.function.sql',
                   trunk_dir + '\\UserFunctions\\dbo.udf_GetCustomerIdentityForLicense.function.sql',

                   trunk_dir + '\\UserFunctions\\dbo.udf_GetCustomerDisability.function.sql',
                   trunk_dir + '\\Views\\dbo.vw_rpt_CustomerIndividual.view.sql',
                   trunk_dir + '\\Views\\dbo.Diag_ItemFeeDist_PercentageTotals.view.sql',
                   trunk_dir + '\\Views\\dbo.vw_CustomerActiveID.view.sql',
                   trunk_dir + '\\Views\\dbo.Diag_ItemFeeDist_UnallocatedTotals.view.sql',
                   ]
    enum_list = get_enums(trunk_dir + '\\Views')
    file_loc = trunk_dir + '\\Enums'
    fh.clear_folder(file_loc)
    fh.move_files(enum_list, file_loc)
    if os.path.exists(trunk_dir):
        script_file = os.path.join(trunk_dir, script_name)
        fh.write_file(script_file, '')
        for folder in child_folders:
            abs_path = os.path.join(trunk_dir, folder)
            if folder == 'SpecialScripts':
                merge_special_scripts(moved_files, script_file)
                file_loc = trunk_dir + '\\SpecialScripts'
                fh.clear_folder(file_loc)
                fh.move_files(moved_files, file_loc)
                continue
            if folder == 'Views':
                merge_views(view_list, abs_path, script_file)
                continue
            if os.path.exists(abs_path):
                files = os.listdir(abs_path)
                for file in files:
                    f = os.path.join(abs_path, file)
                    if os.path.isfile(f):
                        context = fh.read_file(f)
                        context = "\r\n" + context
                        fh.write_file(script_file, context, 'utf-8', 'a')


def main():
    cons.run()
    fk.run()
    func.run()
    idx.run()
    pk.run()
    sp.run()
    tb.run()
    tr.run()
    uk.run()
    vw.run()
    merge_all_scripts()
    print('merge comppleted')


main()




