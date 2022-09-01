from py4j.java_gateway import JavaGateway
import json

gateway = JavaGateway()

entryPoint = gateway.entry_point

handler = entryPoint.getStoreHandler()
collector = entryPoint.getJavaCollector()



def get_current_package_number():

    return collector.get_current_package_number()

def get_next_package_number():

    return collector.getNextPackageNumber()

def get_package():
    list = collector.getPackage("my","Package")

    return list

    
def get_graph():
    grap = collector.getGraph("my")

    return grap

