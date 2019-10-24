package com.example.demo.user.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.user.dto.Authorities;

public interface AuthoritiesRepository extends JpaRepository<Authorities, String>{

}
