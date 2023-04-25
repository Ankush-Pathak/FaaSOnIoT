package com.example.demo.Controllers;

import com.example.demo.Model.Schema;
import com.example.demo.Repository.SchemaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;


@CrossOrigin(origins = "http://localhost:8082")
@RestController
@RequestMapping("/dbInsert")
public class SchemaController {

    @Autowired
    SchemaRepository sr;

    @PostMapping("/insert")
    public ResponseEntity<Schema> createTutorial(@RequestBody Schema s) {

        try {
            Schema _schema;
            _schema = sr
                    .save(new Schema(s.getId(), s.getName(), s.getVersion(), s.getRuntimeEnvironment(),
                            s.getRun_containerized(), s.getRequiredPlatform(), s.getPubs_Topic(), s.getSubsTopic(),
                            s.getExecCommands(), s.getWaitForExit(), s.getMode(), s.getDependencies()));
            return new ResponseEntity<>(_schema, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/getContent")
    public ResponseEntity<List<Schema>> getAllTutorials(@RequestParam(required = false) String title) {
        try {
            List<Schema> schemaList = new ArrayList<Schema>();
            sr.findAll();
            System.out.println(sr.findAll());
            if (schemaList.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(schemaList, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
