package com.example.demo.log.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.example.demo.log.dto.Log;
import com.example.demo.log.dto.LogPageView;
import com.example.demo.log.service.LogService;

import lombok.extern.slf4j.Slf4j;

@CrossOrigin
@Controller
@Slf4j
public class LogController {
	@Autowired
	private LogService logService;
	
	// 페이지에 대한 로그 저장
    @PostMapping("/log.do")
    public ResponseEntity<String> homeLog(@RequestBody Log logData) {
        log.debug(logData.getPageName() + " 페이지 호출");
        logService.homeLog(logData);
        return new ResponseEntity<String>("성공", HttpStatus.OK);
    }

    // 로그 리스트 조회
    @GetMapping("/getLog.do")
    public ResponseEntity<LogPageView> getLog(){
    	log.debug("log 페이지 호출");
    	return new ResponseEntity<LogPageView>(logService.getLog(), HttpStatus.OK);
    }
}
