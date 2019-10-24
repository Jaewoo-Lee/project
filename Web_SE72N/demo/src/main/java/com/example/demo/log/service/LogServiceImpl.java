package com.example.demo.log.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import com.example.demo.log.dto.Log;
import com.example.demo.log.dto.LogPageView;
import com.example.demo.log.repository.LogRepository;

@Service
public class LogServiceImpl implements LogService {
	@Autowired
	private LogRepository logRepository;
	
	@Override
	public void homeLog(Log logData) {
		logRepository.save(logData);
	}

	@Override
	public LogPageView getLog() {
		LogPageView temp = new LogPageView();
		temp.setLogList(logRepository.findAll(new Sort(Sort.Direction.DESC, "logDatetime")));
		temp.setLogTotalList(logRepository.findCount());
		return temp;
	}

}
