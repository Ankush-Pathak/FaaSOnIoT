package com.example.demo.Controllers;

public class configurationFileObject {
    String name;
    String version;
    String runtime;
//     String[] rpt;
//     String rst;
    resourcesClassObject resources;
//
//    @SuppressWarnings("unchecked")
//    @JsonProperty("resources")
//    private void unpackNested(Map<String,Object> resources) {
//        this.rpt = (String)resources.get("publishTo");
//        this.rst = (String)resources.get("subscribeTo");
////        Map<String,String> owner = (Map<String,String>)brand.get("owner");
////        this.ownerName = owner.get("name");
//    }
    String platform;
    String containerized;
    String commandsToRun;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

//    public String getRst() {
//        return rst;
//    }
//
//    public void setRst(String rpt) {
//        this.rpt = rst;
//
//
//    public String getRpt() {
//        return rpt;
//    }
//
//    public void setRpt(String rpt) {
//        this.rpt = rpt;
//    }
//
    public resourcesClassObject getResources() {
        return resources;
    }

    public void setResources(resourcesClassObject resources) {
        this.resources = resources;
    }


//    public String getPublishTo() {
//        return resources.publishTo;
//    }
//
//    public void setPublishTo(resourcesClassObject resources) {
//        this.resources.publishTo = resources.publishTo;
//    }
//
//    public String getSubscribeTo() {
//        return resources.subscribeTo;
//    }
//
//    public void setSubscribeTo(resourcesClassObject resources) {
//        this.resources.subscribeTo = resources.subscribeTo;
//    }


    public String getRuntime() {
        return runtime;
    }

    public void setRuntime(String runtime) {
        this.runtime = runtime;
    }

    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }

    public String getContainerized() {
        return containerized;
    }

    public void setContainerized(String containerized) {
        this.containerized = containerized;
    }

    public String getCommandsToRun() {
        return commandsToRun;
    }

    public void setCommandsToRun(String commandsToRun) {
        this.commandsToRun = commandsToRun;
    }
}

