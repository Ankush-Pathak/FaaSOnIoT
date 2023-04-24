package com.example.demo.Model;

import jakarta.persistence.*;

@Entity
@Table(name = "schema")
public class Schema {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Column(name = "name")
    String name;
    @Column(name = "version")
    String version;
    @Column(name = "runtimeEnvironment")
    String runtimeEnvironment;
    @Column(name = "requiredPlatform")
    String requiredPlatform;

    @Column(name = "run_containerized")
    boolean run_containerized;

    @Column(name = "dependencies")
    String dependencies;

    @Column(name = "subsTopic")
    String subsTopic;
    @Column(name = "Pubs_Topic")
    String Pubs_Topic;
    @Column(name = "mode")
    String mode;
    @Column(name = "execCommands")
    String execCommands;
    @Column(name = "waitForExit")
    String waitForExit;

    public Schema() {

    }

    public Schema(String name, String version, String runtimeEnvironment,
                  String requiredPlatform, boolean run_containerized,
                  String dependencies, String subsTopic, String Pubs_Topic, String mode,
                  String waitForExit, String execCommands) {
        this.name = name;//done
        this.version = version;//done
        this.runtimeEnvironment = runtimeEnvironment;//done
        this.requiredPlatform = requiredPlatform;//done
        this.run_containerized = run_containerized;//done
        this.dependencies = dependencies;//done
        this.subsTopic = subsTopic;//done
        this.Pubs_Topic=Pubs_Topic;//done
        this.mode=mode;//done
        this.waitForExit=waitForExit;//done
        this.execCommands=execCommands;
    }
    //getters and setters for all variables
    public long getId() {
        return id;
    }

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
        this.name = version;
    }

    public String getRuntimeEnvironment() {
        return runtimeEnvironment;
    }
    public void setRuntimeEnvironment(String runtimeEnvironment) {
        this.name = runtimeEnvironment;
    }

    public String getRequiredPlatform() {
        return requiredPlatform;
    }
    public void setRequiredPlatform (String requiredPlatform) {
        this.requiredPlatform = requiredPlatform;
    }

    public boolean getRun_containerized() {
        return run_containerized;
    }
    public void setRun_containerized(boolean run_containerized) {
        this.run_containerized = run_containerized;
    }

    public String setDependencies() {
        return dependencies;
    }
    public void getDependencies(boolean depenedencies) {
        this.dependencies = dependencies;
    }

    public String getSubsTopic() {
        return subsTopic;
    }
    public void setSubsTopicStrings(String subsTopic) {
        this.subsTopic = subsTopic;
    }

    public String getPubs_Topic() {
        return Pubs_Topic;
    }
    public void setPubsTopicStrings(String Pubs_Topic) {
        this.Pubs_Topic = Pubs_Topic;
    }

    public String getMode(String mode) {
        return mode;
    }
    public void setMode(String mode) {
        this.mode = mode;
    }

    public String getWaitForExit(String waitForExit) {
        return waitForExit;
    }
    public void setWaitForExit(String waitForExit) {
        this.waitForExit = waitForExit;
    }

    public String getExecCommands(String execCommands) {
        return execCommands;
    }
    public void setExecCommands(String execCommands) {
        this.execCommands = execCommands;
    }




}

// Shubham's Class.

//class Schema(Base):
//
//        _tablename_ = "schema"
//
//
//        id =  Column(Integer, primary_key = True)
//        name    =  Column(String(30))
//        version    =  Column(String(30))
//
//
//
//
//        runtimeEnvironment     =  Column(String(30))
//        requiredPlatform     =  Column(String(30))
//        run_containerized  =  Column(Boolean, unique=False, default=True)
//
//        dependecies     =  Column(String(30))
//
//        subsTopic     =  Column(String(30))
//
//        Pubs_Topic     =  Column(String(30))
//
//
//        mode     =  Column(String(30))
//        execCommands     =  Column(String(30))
//
//        waitForExit     =  Column(String(30))
//
//
//        status     =  Column(String(30))
//
//        deInternalStatus     =  Column(String(30))
//
//        process = relationship('Process', back_populates='schema')
//
//        stats = relationship('Stats', back_populates='stats')
//
//
//
//
//
//
//class Process(Base):
//        _tablename_ = "process"
//
//        id   =  Column(Integer, primary_key = True)
//        cmd     =  Column(String(30))
//        status     =  Column(String(30))
//        statusInfo     =  Column(String(30))
//
//        process_id = Column(Integer, ForeignKey('schema.id'))
//
//
//        schema = relationship('Schema', back_populates='process')
//
//
//class Stats(Base):
//        _tablename_ = "stats"
//
//        id  =  Column(Integer, primary_key=True)
//        msgPublished  =  Column(Integer)
//        msgSentToOpp   =  Column(Integer)
//        resourceUsage   =  Column(Float)
//
//        stats_id = Column(Integer, ForeignKey('schema.id'))
//
//        stats = relationship('Schema', back_populates='stats')