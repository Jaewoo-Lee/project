package com.example.demo.log.repository;

import java.util.List;
import java.util.Map;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.example.demo.log.dto.Log;

public interface LogRepository extends JpaRepository<Log, Integer>{
	@Query(value = "SELECT new Map(pageName as pageName, COUNT(*) AS pageCount) FROM Log GROUP BY pageName")
	public List<Map<String, Object>> findCount();
}
