CREATE DATABASE [RappiML]
GO

USE [RappiML]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ordersClassification](
	[order_id] [bigint] NOT NULL,
	[store_id] [bigint] NULL,
	[created_at] [datetime] NULL,
	[to_user_distance] [float] NULL,
	[to_user_elevation] [float] NULL,
	[total_earning] [float] NULL,
	[taken] [bit] NOT NULL,
	[probability] [float] NOT NULL
) ON [PRIMARY]
GO


