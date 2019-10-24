package com.example.demo.log.dto;

import java.util.List;
import java.util.Map;

import lombok.Data;

@Data
public class LogPageView {
	private List<Log> logList;
	private List<Map<String, Object>> logTotalList;
}
