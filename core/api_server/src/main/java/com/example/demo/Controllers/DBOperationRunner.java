package com.example.demo.Controllers;

import com.example.demo.Repository.SchemaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.boot.CommandLineRunner;
@Component
public abstract class DBOperationRunner implements CommandLineRunner{

    @Autowired
    SchemaRepository sRepo;


}
