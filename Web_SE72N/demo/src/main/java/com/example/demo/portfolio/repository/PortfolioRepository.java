package com.example.demo.portfolio.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.portfolio.dto.Portfolio;

public interface PortfolioRepository extends JpaRepository<Portfolio, Integer>{

}
