import psycopg2
import os
import logging
from app.models import TelemetryUser

class Database():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(os.getenv("DATABASE_URL"))
            logging.info("Connection success")
        except Exception as e:
            logging.error(f"Database connection failed: {e}")
            self.conn = None

    def init_db(self):
        if not self.conn:
            raise Exception("Cannot initialize DB: No active connection")
            
        init_query = """
        CREATE TABLE IF NOT EXISTS telemetry_users (
            id BIGSERIAL PRIMARY KEY,
            uuid UUID NOT NULL,
            timestamp TIMESTAMPTZ NOT NULL,
            system VARCHAR(100) NOT NULL
        );
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(init_query)
                
    def get_db(self):

        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        try:
            yield conn
        finally:
            conn.close()
            
    def insert_user(self, conn, user: TelemetryUser):
        insert_query = """
        INSERT INTO telemetry_users (uuid, timestamp, system)
        VALUES (%s, %s, %s);
        """
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    insert_query, 
                    (
                        str(user.uuid),
                        user.timestamp, 
                        user.system
                    )
                )
    def get_telemetry_stats(self, conn):
        query = """
        WITH stats AS (
            SELECT 
                COUNT(*) as total_count,
                COUNT(*) FILTER (WHERE timestamp >= CURRENT_DATE) as today_count
            FROM telemetry_users
        ),
        systems AS (
            SELECT 
                system,
                ROUND((COUNT(*)::NUMERIC / (SELECT COUNT(*) FROM telemetry_users)) * 100, 2) as percentage
            FROM telemetry_users
            GROUP BY system
        )
        SELECT 
            s.total_count,
            s.today_count,
            COALESCE(jsonb_object_agg(sys.system, sys.percentage), '{}'::jsonb) as system_distribution
        FROM stats s
        CROSS JOIN systems sys
        GROUP BY s.total_count, s.today_count;
        """
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                
                if not row or row[0] is None:
                    return {
                        "total_users": 0,
                        "today_users": 0,
                        "systems_percentage": {}
                    }
                
                return {
                    "total_users": row[0],
                    "today_users": row[1],
                    "systems_percentage": row[2]
                }
