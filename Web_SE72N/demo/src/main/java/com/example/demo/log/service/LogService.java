package com.example.demo.log.service;

import com.example.demo.log.dto.Log;
import com.example.demo.log.dto.LogPageView;

public interface LogService {
	public void homeLog(Log logData);
	public LogPageView getLog();

}
