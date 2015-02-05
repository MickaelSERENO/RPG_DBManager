from gi.repository import Gtk, GObject, Gdk
from databaseFunctions import *
from globalVar import *
from FileManager import FileManager
from BestiaryTab import BestiaryTab
from EditPower import EditPower
from ArmoryTab import ArmoryTab
from EditType import EditType
from CreateWindowDatas import *

class DatabaseWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Database Manager")
        self.fileManager = FileManager()
        self.handlePower = EditPower()
        self.bestiaryTab = BestiaryTab()
        self.armoryTab   = ArmoryTab(self)
        self.editType    = EditType(self.bestiaryTab, self.armoryTab)

        vbox    = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #Init actions
        self.actionGroup = Gtk.ActionGroup("Actions")
        self.makeFileMenuAction()
        self.makeEditionMenuAction()
        self.makeToolbarAction()
        self.uiManager   = self.createUIManager()
        self.uiManager.insert_action_group(self.actionGroup)

        self.notebook         = Gtk.Notebook()
        self.notebook.set_size_request(600, 300)

        self.notebook.append_page(self.bestiaryTab, Gtk.Label("Bestiary"))
        self.notebook.append_page(self.armoryTab, Gtk.Label("Armory"))

        vbox.pack_start(self.uiManager.get_widget("/MenuBar"), False, False, 0)
        vbox.pack_start(self.uiManager.get_widget("/ToolBar"), False, False, 0)
        vbox.pack_start(self.notebook, True, True, 0)

        self.add(vbox)

        self.show_all()

    def makeFileMenuAction(self):
        fileMenuAction = Gtk.Action("FileMenu", "_File", None, None)
        self.actionGroup.add_action(fileMenuAction)

        newFileAction  = Gtk.Action("NewFile", "_New File", None, Gtk.STOCK_NEW)
        self.actionGroup.add_action_with_accel(newFileAction, "<Ctrl>n")
        newFileAction.connect("activate", self.newFile)

        openFileAction = Gtk.Action("OpenFile", "_Open File", None, Gtk.STOCK_OPEN)
        self.actionGroup.add_action_with_accel(openFileAction, "<Ctrl>o")
        openFileAction.connect("activate", self.openFile)

        saveAction     = Gtk.Action("Save", "_Save", None, Gtk.STOCK_SAVE)
        self.actionGroup.add_action_with_accel(saveAction, "<Ctrl>s")
        saveAction.connect("activate", self.save)

        saveAsAction   = Gtk.Action("SaveAs", "_Save As", None, Gtk.STOCK_SAVE_AS)
        self.actionGroup.add_action_with_accel(saveAsAction, "<Ctrl><Shift>s")
        saveAsAction.connect("activate", self.saveAs)

    def makeEditionMenuAction(self):
        editionMenuAction = Gtk.Action("EditMenu", "_Edit", None, None)
        self.actionGroup.add_action(editionMenuAction)

        editPowerAction = Gtk.Action("EditPower", "Edit _Power", None, None)
        self.actionGroup.add_action_with_accel(editPowerAction, "<Ctrl>p")
        editPowerAction.connect("activate", self.editPower)

        editTypeAction  = Gtk.Action("EditType", "Edit _Type", None, None)
        self.actionGroup.add_action_with_accel(editTypeAction, "<Ctrl>t")
        editTypeAction.connect("activate", self.editList)

    def makeToolbarAction(self):
        toolsMenuAction = Gtk.Action("ToolsMenu", "_Tools", None, None)
        self.actionGroup.add_action(toolsMenuAction)

        addAction = Gtk.Action("Add", "_Add", None, Gtk.STOCK_ADD)
        self.actionGroup.add_action_with_accel(addAction, "<Ctrl>a")
        addAction.connect("activate", self.addItem)

        deleteAction = Gtk.Action("Delete", "_Delete", None, None)
        self.actionGroup.add_action_with_accel(deleteAction, "<Ctrl>d")
        deleteAction.connect("activate", self.deleteItem)
        deleteAction.set_icon_name("eraser")

        clearAction = Gtk.Action("Clear", "_Clear", None, Gtk.STOCK_CLEAR)
        self.actionGroup.add_action_with_accel(clearAction, "<Ctrl>c")
        clearAction.connect("activate", self.clearItems)

    def createUIManager(self):
        with open("Ressources/UI_INFO.xml", 'r') as info:
            ui = Gtk.UIManager()
            ui.add_ui_from_string(info.read())
            self.add_accel_group(ui.get_accel_group())
            return ui

    def newFile(self, widget):
        pass

    def openFile(self, widget):
        self.fileManager.openFile(self.bestiaryTab, self.armoryTab, self.handlePower)

    def saveAs(self, widget):
        self.fileManager.saveAs(self.bestiaryTab, self.armoryTab, self.handlePower)

    def save(self, widget):
        self.fileManager.saveFile(self.bestiaryTab, self.armoryTab, self.handlePower)

    def addItem(self, widget):
        pass

    def deleteItem(self, widget):
        self.notebook.get_nth_page(self.notebook.get_current_page()).deleteEntry()

    def clearItems(self, widget):
        self.notebook.get_nth_page(self.notebook.get_current_page()).clearEntry()

    def editPower(self, widget):
        self.handlePower.editList()

    def editList(self, widget):
        self.editType.editList()