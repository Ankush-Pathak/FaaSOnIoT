package com.example.demo.Controllers;

import com.example.demo.Model.Schema;
import com.example.demo.Repository.SchemaRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import net.lingala.zip4j.ZipFile;
import net.lingala.zip4j.exception.ZipException;
import org.apache.tomcat.util.http.fileupload.IOUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;

@RestController
public class ApiControllers {

    @PostMapping("/create")
    public String add(@RequestParam("file") MultipartFile file) throws IOException {


        /**
         * save file to temp
         */
        File zip = File.createTempFile(UUID.randomUUID().toString(), "temp");
        FileOutputStream o = new FileOutputStream(zip);
        IOUtils.copy(file.getInputStream(), o);
        o.close();

        /**
         * unizp file from temp by zip4j
         */
        String destination = "/Users/mohitdalvi/Desktop/FaasOnIoT";
        try {
            ZipFile zipfile = new ZipFile(zip);
            zipfile.extractAll(destination);

            //sanity check for checking requirements.txt
//            String splittedbefore = zipfile.getFileHeaders().toString();
//            for (int i = 0; i < zipfile.getFileHeaders().size(); i++)
//            {
//                String splitted = zipfile.getFileHeaders().get(i).toString();
//                 //Arrays.stream(splitted.split("/")).toList();
//                System.out.println(Arrays.stream(splitted.split("/")).toList().getClass());
//            }
            int configPresent =0; // flag to check if config file present.
            for (int i = 0; i < zipfile.getFileHeaders().size(); i++)
            {
                String splitted = zipfile.getFileHeaders().get(i).toString();
                //listed file name and used split by / to see if config file is present
                //System.out.println(splitted[splitted.length-1]);
                //System.out.println(splitted[splitted.length-1]);
                //The above code gets the extracted folder and lists all the filenames in it.
                // U must check whether the config file is present and perform sanity checks on it.
                if (splitted.contains("/app.config"))
                {
                    configPresent = 1;
                    File configFileObj = new File("/Users/mohitdalvi/Desktop/FaasOnIoT/" + splitted);
                    System.out.println("Config file is present");
                    System.out.println(configFileObj);
                    //for (int j=0; j<extractedFiles.listFiles()[i].toString().split("/").length;j++)
                    //{}
                    //if (extractedFiles.listFiles()[i].toString().split("/")[-1]=="/Users/mohitdalvi/Desktop/FaasOnIoT/AppMetrics-features-4.4.0/NuGet.config")

                    // Sanity Checks on congif File:
                    // 1. Check if Application name is present
                    ObjectMapper mapper = new ObjectMapper();

                    configurationFileObject cfo = mapper.readValue(new File("/Users/mohitdalvi/Desktop/FaasOnIoT/" + splitted), configurationFileObject.class);
                    System.out.println(cfo);

                    if (cfo.name.equals(""))
                    {
                        System.out.println("Application name is NUll");
                        return " ERROR";
                    } else{System.out.println("Application name received");System.out.println(cfo.name);}
                    //2. Check if version is present
                    if (cfo.version.equals(""))
                    {
                        System.out.println("Version name is NUll");
                        return "Error";
                    }else{System.out.println("Version name received");}
                    // 3.Check if this application is publishing to a topic or subscribing to a topic
                    System.out.println(Arrays.stream(cfo.resources.PublishTo()).toList());

                    // 4. Check if user has specified the platform on which the application has to be deployed
                    if (cfo.platform.equals(""))
                    {
                        System.out.println("Platform name is NUll");
                        return "Error";

                    }else
                    {
                        if(cfo.platform.equals("L4") || cfo.platform.equals("BeagleBoneBlack") || cfo.platform.equals("Linux"))
                        {
                            System.out.println("Platform received");
                        }
                        else{
                            System.out.println("Incorrect platform  name ");
                        }
                    }
                    // 5, Should it be run in a containerized environment or not
                    if (cfo.containerized.equals(""))
                    {
                        System.out.println("Did not specify whether to containerize");
                        return "Error";
                    }else
                    {
                        if(cfo.containerized.equals("Yes") || cfo.containerized.equals("No"))
                        {
                            System.out.println("Containerization status received");
                        }
                        else{
                            System.out.println("Please specify containerization as Yes or No");
                            return "Error";
                        }
                    }
                    // 6. User must specify the commands to run thr application
                    if (cfo.commandsToRun.equals(""))
                    {
                        System.out.println("Please specify the commands to run the application");
                        return " ERROR";
                    } else{System.out.println("Commands to run received");}

                    // if all the sanity checks satisfy then we can post the content into the database


                    SchemaRepository sRepo = ;
                    sRepo.saveAll();

                }
            }
            if (configPresent==1)
            {
                return "configPresent";
            }
            else {
                return "config not Present";
            }

        } catch (ZipException e) {
            e.printStackTrace();
        } finally {
            /**
             * delete temp file
             */
            zip.delete();
        }

        return "redirect:/";
    }
}
