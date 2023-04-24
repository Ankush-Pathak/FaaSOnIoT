package com.example.demo.Repository;


import com.example.demo.Model.Schema;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SchemaRepository extends JpaRepository<Schema,String> {

//    //custom methods
//    List<Schema> findByPublished(boolean published);
//    List<Schema> hello(String name);
}
